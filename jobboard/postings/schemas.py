from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Union


class JobPosting(BaseModel):
    title: str
    description: str = Field(alias='content') # Maps 'content' from JSON to 'description'
    hiring_organization: str = Field(alias='company_name')
    job_location: list[str]
    date_posted: datetime = Field(alias='first_published')
    valid_through: Optional[datetime] = None
    employment_type: Optional[str] = None
    base_salary: Optional[Union[int, str]] = None
    requirements: list[str] = []
    experience_years: Optional[int] = None
    education_requirements: Optional[str] = None