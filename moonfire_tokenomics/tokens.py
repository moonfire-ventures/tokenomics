from enum import Enum

from moonfire_tokenomics.data.admc import admc
from moonfire_tokenomics.data.amp import amp
from moonfire_tokenomics.data.ampl import ampl
from moonfire_tokenomics.data.anc import anc
from moonfire_tokenomics.data.aot import aot
from moonfire_tokenomics.data.atlas import atlas
from moonfire_tokenomics.data.axs import axs
from moonfire_tokenomics.data.badger import badger
from moonfire_tokenomics.data.bcmc import bcmc
from moonfire_tokenomics.data.bcoin import bcoin
from moonfire_tokenomics.data.bnt import bnt
from moonfire_tokenomics.data.bnx import bnx
from moonfire_tokenomics.data.byg import byg
from moonfire_tokenomics.data.chz import chz
from moonfire_tokenomics.data.crv import crv
from moonfire_tokenomics.data.dodo import dodo
from moonfire_tokenomics.data.dxct import dxct
from moonfire_tokenomics.data.dydx import dydx
from moonfire_tokenomics.data.elfin import elfin
from moonfire_tokenomics.data.els import els
from moonfire_tokenomics.data.fara import fara
from moonfire_tokenomics.data.farm import farm
from moonfire_tokenomics.data.gem import gem
from moonfire_tokenomics.data.gmee import gmee
from moonfire_tokenomics.data.gods import gods
from moonfire_tokenomics.data.he import he
from moonfire_tokenomics.data.i1nch import i1nch
from moonfire_tokenomics.data.ilv import ilv
from moonfire_tokenomics.data.isky import isky
from moonfire_tokenomics.data.link import link
from moonfire_tokenomics.data.lrc import lrc
from moonfire_tokenomics.data.mana import mana
from moonfire_tokenomics.data.mbox import mbox
from moonfire_tokenomics.data.meta import meta
from moonfire_tokenomics.data.mft import mft
from moonfire_tokenomics.data.mir import mir
from moonfire_tokenomics.data.ngl import ngl
from moonfire_tokenomics.data.pgx import pgx
from moonfire_tokenomics.data.polis import polis
from moonfire_tokenomics.data.pols import pols
from moonfire_tokenomics.data.quick import quick
from moonfire_tokenomics.data.ray import ray
from moonfire_tokenomics.data.ren import ren
from moonfire_tokenomics.data.revv import revv
from moonfire_tokenomics.data.rune import rune
from moonfire_tokenomics.data.sand import sand
from moonfire_tokenomics.data.scream import scream
from moonfire_tokenomics.data.slnd import slnd
from moonfire_tokenomics.data.spell import spell
from moonfire_tokenomics.data.sps import sps
from moonfire_tokenomics.data.srm import srm
from moonfire_tokenomics.data.tita import tita
from moonfire_tokenomics.data.tower import tower
from moonfire_tokenomics.data.uma import uma
from moonfire_tokenomics.data.uni import uni
from moonfire_tokenomics.data.yfi import yfi
from moonfire_tokenomics.data.zrx import zrx


class Tokens(Enum):
    # defi
    UNI = uni
    I1NCH = i1nch
    LINK = link
    RAY = ray
    SLND = slnd
    SCREAM = scream
    DYDX = dydx
    BNT = bnt
    RUNE = rune
    AMP = amp
    LRC = lrc
    ZRX = zrx
    CRV = crv
    QUICK = quick
    SPELL = spell
    ANC = anc
    SRM = srm
    POLS = pols
    FARM = farm
    MFT = mft
    MIR = mir
    BADGER = badger
    DODO = dodo
    REN = ren
    UMA = uma
    YFI = yfi
    AMPL = ampl

    # gaming
    MANA = mana
    AXS = axs
    SAND = sand
    SPS = sps
    POLIS = polis
    ATLAS = atlas
    NGL = ngl
    TITA = tita
    HE = he
    ILV = ilv
    ISKY = isky
    CHZ = chz
    GODS = gods
    GEM = gem
    PGX = pgx
    BCOIN = bcoin
    MBOX = mbox
    TOWER = tower
    GMEE = gmee
    META = meta
    ELFIN = elfin
    FARA = fara
    DXCT = dxct
    BYG = byg
    AOT = aot
    BNX = bnx
    BCMC = bcmc
    REVV = revv
    ADMC = admc
    ELS = els

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
