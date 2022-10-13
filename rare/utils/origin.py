
import winreg
from typing import Optional

from legendary.models.game import Game
from legendary.utils import windows_helpers


def get_install_path(game: Game) -> Optional[str]:
    reg_path = game.metadata \
        .get("customAttributes", {}) \
        .get("RegistryPath", {}).get("value", None)
    if not reg_path:
        return None
    return windows_helpers.query_registry_value(winreg.HKEY_LOCAL_MACHINE, reg_path, "Install Dir")


def is_origin_game(game: Game) -> bool:
    return game.metadata \
               .get("customAttributes", {}) \
               .get("ThirdPartyManagedApp", {}) \
               .get("value") == "Origin"


def is_installed(game: Game):
    return get_install_path(game) is not None
