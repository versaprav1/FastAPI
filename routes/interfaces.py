from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_db

router = APIRouter(prefix="/api", tags=["interfaces"])

@router.get("/tables")
async def get_tables(db: Session = Depends(get_db)):
    """Get list of all available tables"""
    try:
        result = db.execute(
            text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'dev'")
        )
        tables = [row[0] for row in result]
        print("Tables found:", tables)
        return tables
    except Exception as e:
        print("Error fetching tables:", e)
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{table_name}")
async def get_table_data(table_name: str, db: Session = Depends(get_db)):
    """Get data from a specific table"""
    try:
        # Validate table exists
        result = db.execute(
            text("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = 'dev' AND table_name = :table_name)"),
            {"table_name": table_name}
        )
        if not result.scalar():
            raise HTTPException(status_code=404, detail=f"Table '{table_name}' not found in schema 'dev'")

        # Get data from table
        result = db.execute(text(f'SELECT * FROM "dev"."{table_name}"'))
        columns = [col[0] for col in result.cursor.description]
        data = [dict(zip(columns, row)) for row in result]
        print(f"Fetched {len(data)} rows from {table_name}")
        return data
    except Exception as e:
        print(f"Error fetching data from table {table_name}:", e)
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{table_name}/columns")
async def get_table_columns(table_name: str, db: Session = Depends(get_db)):
    """Get column information for a specific table"""
    result = db.execute(text("""
        SELECT column_name, data_type 
        FROM information_schema.columns 
        WHERE table_name = :table_name
    """), {"table_name": table_name})
    
    return [{"name": row[0], "type": row[1]} for row in result]

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload
from db import get_db
from models import (
    AzureTenants as AzureTenant, DataSources as DataSource, # Using aliases to match expected names
    Base # Add other required models with proper aliases as needed
)


@router.get("/tenants/{tenant_id}/subscriptions")
def get_tenant_subscriptions(tenant_id: str, db: Session = Depends(get_db)):
    tenant = db.query(AzureTenant).options(selectinload(AzureTenant.subscriptions)).filter(AzureTenant.id == tenant_id).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return [sub.id for sub in tenant.subscriptions]

@router.get("/subscriptions/{subscription_id}/tenant")
def get_subscription_tenant(subscription_id: str, db: Session = Depends(get_db)):
    from models import AzureSubscription
    sub = db.query(AzureSubscription).options(selectinload(AzureSubscription.tenant)).filter(AzureSubscription.id == subscription_id).first()
    if not sub:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return {"tenant_id": sub.tenant.id if sub.tenant else None}

@router.get("/datasources/{datasource_id}/tenants")
def get_datasource_tenants(datasource_id: str, db: Session = Depends(get_db)):
    datasource = db.query(DataSource).options(selectinload(DataSource.tenants)).filter(DataSource.id == datasource_id).first()
    if not datasource:
        raise HTTPException(status_code=404, detail="DataSource not found")
    return [tenant.id for tenant in datasource.tenants]

@router.get("/tenants/{tenant_id}/datasource")
def get_tenant_datasource(tenant_id: str, db: Session = Depends(get_db)):
    tenant = db.query(AzureTenant).options(selectinload(AzureTenant.data_source)).filter(AzureTenant.id == tenant_id).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return {"datasource_id": tenant.data_source.id if tenant.data_source else None}

# --- New Endpoints for ER Diagram Models ---

@router.get("/resource_groups/{group_id}/integration_accounts")
def get_resource_group_accounts(group_id: str, db: Session = Depends(get_db)):
    group = db.query(AzureResourceGroup).options(selectinload(AzureResourceGroup.integration_accounts)).filter(AzureResourceGroup.id == group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Resource group not found")
    return [acc.id for acc in group.integration_accounts]

@router.get("/integration_accounts/{account_id}/sessions")
def get_account_sessions(account_id: str, db: Session = Depends(get_db)):
    account = db.query(AzureLogicAppIntegrationAccount).options(selectinload(AzureLogicAppIntegrationAccount.sessions)).filter(AzureLogicAppIntegrationAccount.id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Integration account not found")
    return [session.id for session in account.sessions]

@router.get("/integration_accounts/{account_id}/agreements")
def get_account_agreements(account_id: str, db: Session = Depends(get_db)):
    account = db.query(AzureLogicAppIntegrationAccount).options(selectinload(AzureLogicAppIntegrationAccount.agreements)).filter(AzureLogicAppIntegrationAccount.id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Integration account not found")
    return [agr.id for agr in account.agreements]

@router.get("/integration_accounts/{account_id}/certificates")
def get_account_certificates(account_id: str, db: Session = Depends(get_db)):
    account = db.query(AzureLogicAppIntegrationAccount).options(selectinload(AzureLogicAppIntegrationAccount.certificates)).filter(AzureLogicAppIntegrationAccount.id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Integration account not found")
    return [cert.id for cert in account.certificates]

@router.get("/integration_accounts/{account_id}/schemas")
def get_account_schemas(account_id: str, db: Session = Depends(get_db)):
    account = db.query(AzureLogicAppIntegrationAccount).options(selectinload(AzureLogicAppIntegrationAccount.schemas)).filter(AzureLogicAppIntegrationAccount.id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Integration account not found")
    return [schema.id for schema in account.schemas]

@router.get("/integration_accounts/{account_id}/maps")
def get_account_maps(account_id: str, db: Session = Depends(get_db)):
    account = db.query(AzureLogicAppIntegrationAccount).options(selectinload(AzureLogicAppIntegrationAccount.maps)).filter(AzureLogicAppIntegrationAccount.id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Integration account not found")
    return [m.id for m in account.maps]

@router.get("/integration_accounts/{account_id}/partners")
def get_account_partners(account_id: str, db: Session = Depends(get_db)):
    account = db.query(AzureLogicAppIntegrationAccount).options(selectinload(AzureLogicAppIntegrationAccount.partners)).filter(AzureLogicAppIntegrationAccount.id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Integration account not found")
    return [p.id for p in account.partners]

@router.get("/integration_accounts/{account_id}/partner_metadata")
def get_account_partner_metadata(account_id: str, db: Session = Depends(get_db)):
    account = db.query(AzureLogicAppIntegrationAccount).options(selectinload(AzureLogicAppIntegrationAccount.partner_metadata)).filter(AzureLogicAppIntegrationAccount.id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Integration account not found")
    return [pm.id for pm in account.partner_metadata]

@router.get("/integration_accounts/{account_id}/partner_identities")
def get_account_partner_identities(account_id: str, db: Session = Depends(get_db)):
    account = db.query(AzureLogicAppIntegrationAccount).options(selectinload(AzureLogicAppIntegrationAccount.partner_identities)).filter(AzureLogicAppIntegrationAccount.id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Integration account not found")
    return [pi.id for pi in account.partner_identities]

@router.get("/workflows/{workflow_id}/versions")
def get_workflow_versions(workflow_id: str, db: Session = Depends(get_db)):
    workflow = db.query(AzureLogicAppWorkflow).options(selectinload(AzureLogicAppWorkflow.workflow_versions)).filter(AzureLogicAppWorkflow.id == workflow_id).first()
    if not workflow:
        raise HTTPException(status_code=404, detail="Workflow not found")
    return [wv.id for wv in workflow.workflow_versions]

@router.get("/standard_apps/{app_id}/workflows")
def get_standard_app_workflows(app_id: str, db: Session = Depends(get_db)):
    app = db.query(AzureStandardApp).options(selectinload(AzureStandardApp.workflows)).filter(AzureStandardApp.id == app_id).first()
    if not app:
        raise HTTPException(status_code=404, detail="Standard App not found")
    return [w.id for w in app.workflows]

# --- Azure API Management Endpoints ---
from pydantic import BaseModel
from typing import List, Optional

class ApiManagementApiOut(BaseModel):
    id: str
    create_time: Optional[str]
    change_time: Optional[str]
    name: Optional[str]
    location: Optional[str]
    service_url: Optional[str]
    service_id: Optional[str]
    class Config:
        orm_mode = True

class ApiManagementServiceOut(BaseModel):
    id: str
    resource_group_id: Optional[str]
    data_source_id: Optional[str]
    apis: List[ApiManagementApiOut] = []
    class Config:
        orm_mode = True

@router.get("/api_management_services/{service_id}/apis", response_model=ApiManagementServiceOut)
def get_apis_for_service(service_id: str, db: Session = Depends(get_db)):
    service = db.query(AzureApiManagementService).options(selectinload(AzureApiManagementService.apis)).filter(AzureApiManagementService.id == service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="API Management Service not found")
    return service

@router.get("/apis/{api_id}/service", response_model=ApiManagementApiOut)
def get_service_for_api(api_id: str, db: Session = Depends(get_db)):
    api = db.query(AzureApiManagementApi).options(selectinload(AzureApiManagementApi.service)).filter(AzureApiManagementApi.id == api_id).first()
    if not api:
        raise HTTPException(status_code=404, detail="API not found")
    return api