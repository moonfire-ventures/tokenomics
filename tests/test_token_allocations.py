import numpy as np

from moonfire_tokenomics.analysis import tokens_to_df
from moonfire_tokenomics.tokens import Tokens
from moonfire_tokenomics.types import CommonType, Sector


def test_token_allocations():
    data = [token[1] for token in Tokens.choices()]
    _ = tokens_to_df(data)


def test_valid_sector():
    for name, token in Tokens.choices():
        assert token.sector in Sector


def test_sum_between_0_and_1():
    for name, token in Tokens.choices():
        for allocation in token.allocations:
            assert 0 <= np.sum([record.share for record in allocation.records]).round(5) <= 1


def test_shares_between_0_and_1():
    for name, token in Tokens.choices():
        for allocation in token.allocations:
            assert all([0 <= record.share <= 1 for record in allocation.records])


def test_valid_final_allocation():
    """
    Make sure in the final month the allocations sum up to 100%
    """
    for name, token in Tokens.choices():
        sorted_allocation = sorted(token.allocations, key=lambda x: x.month)
        assert np.allclose(sum([record.share for record in sorted_allocation[-1].records]), 1, atol=0.01)


def test_valid_common_type():
    for name, token in Tokens.choices():
        for allocation in token.allocations:
            assert all([record.common_type in CommonType for record in allocation.records])
