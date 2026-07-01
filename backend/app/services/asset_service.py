from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.asset import Asset
from app.schemas.asset import AssetCreate, AssetUpdate


def get_asset_by_id(
    db: Session,
    asset_id: UUID,
) -> Asset | None:
    return db.get(Asset, asset_id)


def get_asset_by_hostname(
    db: Session,
    hostname: str,
) -> Asset | None:
    statement = select(Asset).where(
        Asset.hostname == hostname
    )
    return db.scalar(statement)


def get_assets(
    db: Session,
) -> list[Asset]:
    statement = select(Asset).order_by(
        Asset.hostname
    )
    return list(db.scalars(statement))


def create_asset(
    db: Session,
    asset: AssetCreate,
) -> Asset:
    db_asset = Asset(
        hostname=asset.hostname,
        ip_address=asset.ip_address,
        operating_system=asset.operating_system,
        asset_type=asset.asset_type,
        owner=asset.owner,
        department=asset.department,
        criticality=asset.criticality,
        environment=asset.environment,
    )

    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)

    return db_asset


def update_asset(
    db: Session,
    db_asset: Asset,
    asset: AssetUpdate,
) -> Asset:
    update_data = asset.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(db_asset, field, value)

    db.commit()
    db.refresh(db_asset)

    return db_asset


def delete_asset(
    db: Session,
    db_asset: Asset,
) -> None:
    db.delete(db_asset)
    db.commit()
