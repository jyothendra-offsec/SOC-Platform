from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.asset import (
    AssetCreate,
    AssetResponse,
    AssetUpdate,
)
from app.security.dependencies import get_current_user
from app.services.asset_service import (
    create_asset,
    delete_asset,
    get_asset_by_hostname,
    get_asset_by_id,
    get_assets,
    update_asset,
)

router = APIRouter(
    prefix="/assets",
    tags=["Assets"],
)


@router.post(
    "",
    response_model=AssetResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_new_asset(
    asset: AssetCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if get_asset_by_hostname(db, asset.hostname):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Hostname already exists",
        )

    return create_asset(db, asset)


@router.get(
    "",
    response_model=list[AssetResponse],
)
def list_assets(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return get_assets(db)


@router.get(
    "/{asset_id}",
    response_model=AssetResponse,
)
def get_single_asset(
    asset_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    asset = get_asset_by_id(db, asset_id)

    if asset is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Asset not found",
        )

    return asset


@router.put(
    "/{asset_id}",
    response_model=AssetResponse,
)
def update_existing_asset(
    asset_id: UUID,
    asset_update: AssetUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    asset = get_asset_by_id(db, asset_id)

    if asset is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Asset not found",
        )

    if (
        asset_update.hostname
        and asset_update.hostname != asset.hostname
    ):
        existing = get_asset_by_hostname(
            db,
            asset_update.hostname,
        )

        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Hostname already exists",
            )

    return update_asset(
        db,
        asset,
        asset_update,
    )


@router.delete(
    "/{asset_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def remove_asset(
    asset_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    asset = get_asset_by_id(db, asset_id)

    if asset is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Asset not found",
        )

    delete_asset(
        db,
        asset,
    )
