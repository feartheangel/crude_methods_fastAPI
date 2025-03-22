from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.products import crud
from api_v1.products.dependencies import product_by_id
from api_v1.products.schemas import (
    ProductCreate,
    Product,
    ProductUpdate,
    ProductUpdatePartial,
)
from core.models import db_helper

router = APIRouter(tags=["Products"])


# Get all products
@router.get("/", response_model=list[Product])
async def get_products(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.get_all_products(session=session)


# Create 1 product
@router.post(
    "/create-product", response_model=Product, status_code=status.HTTP_201_CREATED
)
async def create_product(
    product: ProductCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.create_product(session=session, product=product)


# Get 1 product by id
@router.get("/{product_id}", response_model=Product)
async def get_product(product: Product = Depends(product_by_id)):
    return product


# Update full product
@router.put("/{product_id}")
async def update_full_product(
    product_update: ProductUpdate,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Product:
    return await crud.update_full_product(
        session=session,
        product=product,
        product_update=product_update,
    )


# Partial update product
@router.patch("/{product_id}")
async def update_partial_product(
    product_update: ProductUpdatePartial,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Product:
    return await crud.update_partial_product(
        session=session,
        product=product,
        product_update=product_update,
    )


# Delete product by id
@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> None:
    await crud.delete_product(session=session, product=product)
