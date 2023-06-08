# === IMPORTS: BUILT-IN ===

# === IMPORTS: THIRD-PARTY ===

# === IMPORTS: LOCAL ===
from src.configs.myclass_config import MyClassConfig


class MyClass:
    def __init__(self, config: MyClassConfig):
        self.config = config


if __name__ == "__main__":
    pass