from enum import Enum


class ProductType(str, Enum):
    PRODUCT = "product"
    INGREDIENT = "ingredient"
