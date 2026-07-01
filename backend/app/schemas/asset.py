from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.models.asset import (
    AssetType,
    Criticality,
    Environment,
)


class AssetBase(BaseModel):
    hostname: str
    ip_address: str
    operating_system: str

    asset_type: AssetType

    owner: str
    department: str

    criticality: Criticality
    environment: Environment


class AssetCreate(AssetBase):
    pass


class AssetUpdate(BaseModel):
    hostname: str | None = None
    ip_address: str | None = None
    operating_system: str | None = None

    asset_type: AssetType | None = None

    owner: str | None = None
    department: str | None = None

    criticality: Criticality | None = None
    environment: Environment | None = None

    is_active: bool | None = None


class AssetResponse(AssetBase):
    id: UUID

    is_active: bool

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )
