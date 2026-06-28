from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional, Literal

# 1. This models the inner "data" block
class ServiceData(BaseModel):
    slug: str
    name: str
    category: str
    logo_url: HttpUrl        # Validates that this is a proper HTTP/HTTPS URL string
    status: Literal["operational", "degraded", "down"]  # Restricts values to expected states
    official_indicator: Optional[bool] = None          # Allows true, false, or null
    report_count_1h: int
    report_count_24h: int
    status_page_url: HttpUrl # Validates url format
    updated_at: datetime     # Automatically verifies ISO timestamp format


# 2. This models the root JSON response
class StatusResponseModel(BaseModel):
    ok: bool
    data: ServiceData        # Links the nested ServiceData model here