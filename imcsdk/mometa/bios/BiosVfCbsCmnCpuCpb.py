"""This module contains the general information for BiosVfCbsCmnCpuCpb ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCmnCpuCpbConsts:
    VP_CBS_CMN_CPU_CPB_AUTO = "Auto"
    VP_CBS_CMN_CPU_CPB_DISABLED = "Disabled"
    _VP_CBS_CMN_CPU_CPB_DISABLED = "disabled"
    VP_CBS_CMN_CPU_CPB_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCmnCpuCpb(ManagedObject):
    """This is BiosVfCbsCmnCpuCpb class."""

    consts = BiosVfCbsCmnCpuCpbConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCmnCpuCpb", "biosVfCbsCmnCpuCpb", "cpu-cpb", VersionMeta.Version401a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cmn_cpu_cpb": MoPropertyMeta("vp_cbs_cmn_cpu_cpb", "vpCbsCmnCpuCpb", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Auto", "Disabled", "disabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCmnCpuCpb": "vp_cbs_cmn_cpu_cpb", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_cbs_cmn_cpu_cpb = None

        ManagedObject.__init__(self, "BiosVfCbsCmnCpuCpb", parent_mo_or_dn, **kwargs)

