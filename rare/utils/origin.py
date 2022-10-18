import configparser
import os
import platform

from typing import Optional

from legendary.models.game import Game
from rare.shared import LegendaryCoreSingleton


# this is a copied function from legendary.utils.wine_helpers, but it reads system.reg in the wine prefix
def read_system_registry(wine_pfx):
    reg = configparser.ConfigParser(comment_prefixes=(';', '#', '/', 'WINE'), allow_no_value=True,
                                    strict=False)
    reg.optionxform = str
    reg.read(os.path.join(wine_pfx, 'system.reg'))
    return reg


def get_install_path(game: Game) -> Optional[str]:
    reg_path: str = game.metadata \
        .get("customAttributes", {}) \
        .get("RegistryPath", {}).get("value", None)
    if not reg_path:
        return None
    if platform.system() == "Windows":
        import winreg
        from legendary.utils import windows_helpers
        return windows_helpers.query_registry_value(winreg.HKEY_LOCAL_MACHINE, reg_path, "Install Dir")
    else:
        core = LegendaryCoreSingleton()
        wine_prefix = core.lgd.config.get(game.app_name, "wine_prefix", fallback=os.path.expanduser("~/.wine"))
        reg = read_system_registry(wine_prefix)

        # TODO: find a better solution
        reg_path = reg_path.replace("\\", "\\\\").replace("SOFTWARE", "Software").replace("WOW6432Node", "Wow6432Node")

        install_dir = reg.get(reg_path, '"Install Dir"', fallback=None)
        if install_dir:
            return install_dir.strip('"')
        return None


def is_origin_game(game: Game) -> bool:
    return game.metadata \
               .get("customAttributes", {}) \
               .get("ThirdPartyManagedApp", {}) \
               .get("value") == "Origin"


def is_installed(game: Game):
    return get_install_path(game) is not None
