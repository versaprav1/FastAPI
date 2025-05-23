from typing import List, Optional

from sqlalchemy import BigInteger, Boolean, Column, DateTime, ForeignKeyConstraint, Index, LargeBinary, PrimaryKeyConstraint, REAL, SmallInteger, String, Table, Text, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime

class Base(DeclarativeBase):
    pass


class AnypointOrganisations(Base):
    __tablename__ = 'anypoint_organisations'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='anypoint_organisations_pkey'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    key: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    created_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    created_by: Mapped[Optional[str]] = mapped_column(String)
    changed_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    changed_by: Mapped[Optional[str]] = mapped_column(String)

    anypoint_assets: Mapped[List['AnypointAssets']] = relationship('AnypointAssets', back_populates='organisation')


class DataSourceProxies(Base):
    __tablename__ = 'data_source_proxies'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='data_source_proxies_pkey'),
        Index('datasourceproxy_name', 'name', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    url: Mapped[str] = mapped_column(String)
    authentication: Mapped[Optional[str]] = mapped_column(String)

    data_sources: Mapped[List['DataSources']] = relationship('DataSources', back_populates='proxy')
    data_source_basic_auth_credentials: Mapped[List['DataSourceBasicAuthCredentials']] = relationship('DataSourceBasicAuthCredentials', back_populates='proxy')
    data_source_oauth2credentials: Mapped[List['DataSourceOauth2credentials']] = relationship('DataSourceOauth2credentials', back_populates='proxy')
    data_source_proxy_headers: Mapped[List['DataSourceProxyHeaders']] = relationship('DataSourceProxyHeaders', back_populates='proxy')


class DataSources(Base):
    __tablename__ = 'data_sources'
    __table_args__ = (
        ForeignKeyConstraint(['proxy_id'], ['dev.data_source_proxies.id'], ondelete='SET NULL', name='data_sources_data_source_proxies_proxy'),
        ForeignKeyConstraint(['system_id'], ['dev.systems.id'], ondelete='CASCADE', name='data_sources_systems_system'),
        PrimaryKeyConstraint('id', name='data_sources_pkey'),
        Index('datasource_name_type', 'name', 'type', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    category: Mapped[str] = mapped_column(String)
    hostname: Mapped[str] = mapped_column(String)
    system_id: Mapped[str] = mapped_column(String)
    authentication: Mapped[Optional[str]] = mapped_column(String)
    proxy_id: Mapped[Optional[str]] = mapped_column(String)

    proxy: Mapped[Optional['DataSourceProxies']] = relationship('DataSourceProxies', back_populates='data_sources')
    system: Mapped['Systems'] = relationship('Systems', foreign_keys=[system_id], back_populates='data_sources')
    lean_ix_tenants: Mapped[List['LeanIxTenants']] = relationship('LeanIxTenants', back_populates='data_source')
    systems: Mapped[List['Systems']] = relationship('Systems', foreign_keys='[Systems.data_source_id]', back_populates='data_source')
    abap_odata_services: Mapped[List['AbapOdataServices']] = relationship('AbapOdataServices', back_populates='data_source')
    abap_partner_profiles: Mapped[List['AbapPartnerProfiles']] = relationship('AbapPartnerProfiles', back_populates='data_source')
    abap_paths: Mapped[List['AbapPaths']] = relationship('AbapPaths', back_populates='data_source')
    abap_rfc_destinations: Mapped[List['AbapRfcDestinations']] = relationship('AbapRfcDestinations', back_populates='data_source')
    abap_soap_services: Mapped[List['AbapSoapServices']] = relationship('AbapSoapServices', back_populates='data_source')
    abap_systems: Mapped[List['AbapSystems']] = relationship('AbapSystems', back_populates='data_source')
    azure_tenants: Mapped[List['AzureTenants']] = relationship('AzureTenants', back_populates='data_source')
    btp_api_management_products: Mapped[List['BtpApiManagementProducts']] = relationship('BtpApiManagementProducts', back_populates='data_source')
    btp_api_management_providers: Mapped[List['BtpApiManagementProviders']] = relationship('BtpApiManagementProviders', back_populates='data_source')
    btp_cloud_integration_credentials: Mapped[List['BtpCloudIntegrationCredentials']] = relationship('BtpCloudIntegrationCredentials', back_populates='data_source')
    btp_cloud_integration_messages: Mapped[List['BtpCloudIntegrationMessages']] = relationship('BtpCloudIntegrationMessages', back_populates='data_source')
    btp_cloud_integration_packages: Mapped[List['BtpCloudIntegrationPackages']] = relationship('BtpCloudIntegrationPackages', back_populates='data_source')
    btp_cloud_integration_runtime_artefacts: Mapped[List['BtpCloudIntegrationRuntimeArtefacts']] = relationship('BtpCloudIntegrationRuntimeArtefacts', back_populates='data_source')
    btp_event_mesh_queues: Mapped[List['BtpEventMeshQueues']] = relationship('BtpEventMeshQueues', back_populates='data_source')
    btp_event_mesh_topics: Mapped[List['BtpEventMeshTopics']] = relationship('BtpEventMeshTopics', back_populates='data_source')
    btp_tenants: Mapped[List['BtpTenants']] = relationship('BtpTenants', back_populates='data_source')
    data_source_access_tokens: Mapped[List['DataSourceAccessTokens']] = relationship('DataSourceAccessTokens', back_populates='data_source')
    data_source_api_keys: Mapped[List['DataSourceApiKeys']] = relationship('DataSourceApiKeys', back_populates='data_source')
    data_source_basic_auth_credentials: Mapped[List['DataSourceBasicAuthCredentials']] = relationship('DataSourceBasicAuthCredentials', back_populates='data_source')
    data_source_oauth2credentials: Mapped[List['DataSourceOauth2credentials']] = relationship('DataSourceOauth2credentials', back_populates='data_source')
    hopex_tenants: Mapped[List['HopexTenants']] = relationship('HopexTenants', back_populates='data_source')
    inventories: Mapped[List['Inventories']] = relationship('Inventories', back_populates='data_source')
    luy_tenants: Mapped[List['LuyTenants']] = relationship('LuyTenants', back_populates='data_source')
    pro_communication_parties: Mapped[List['ProCommunicationParties']] = relationship('ProCommunicationParties', back_populates='data_source')
    pro_configuration_scenarios: Mapped[List['ProConfigurationScenarios']] = relationship('ProConfigurationScenarios', back_populates='data_source')
    pro_performance_queries: Mapped[List['ProPerformanceQueries']] = relationship('ProPerformanceQueries', back_populates='data_source')
    pro_performance_stats: Mapped[List['ProPerformanceStats']] = relationship('ProPerformanceStats', back_populates='data_source')
    pro_software_components: Mapped[List['ProSoftwareComponents']] = relationship('ProSoftwareComponents', back_populates='data_source')
    tasks: Mapped[List['Tasks']] = relationship('Tasks', back_populates='data_source')
    abap_integration_engine_interfaces: Mapped[List['AbapIntegrationEngineInterfaces']] = relationship('AbapIntegrationEngineInterfaces', back_populates='data_source')
    abap_ports: Mapped[List['AbapPorts']] = relationship('AbapPorts', back_populates='data_source')
    btp_api_management_proxies: Mapped[List['BtpApiManagementProxies']] = relationship('BtpApiManagementProxies', back_populates='data_source')
    btp_cloud_integration_artefacts: Mapped[List['BtpCloudIntegrationArtefacts']] = relationship('BtpCloudIntegrationArtefacts', back_populates='data_source')
    btp_cloud_integration_service_endpoints: Mapped[List['BtpCloudIntegrationServiceEndpoints']] = relationship('BtpCloudIntegrationServiceEndpoints', back_populates='data_source')
    btp_event_mesh_webhooks: Mapped[List['BtpEventMeshWebhooks']] = relationship('BtpEventMeshWebhooks', back_populates='data_source')
    pro_communication_components: Mapped[List['ProCommunicationComponents']] = relationship('ProCommunicationComponents', back_populates='data_source')
    pro_communication_channels: Mapped[List['ProCommunicationChannels']] = relationship('ProCommunicationChannels', back_populates='data_source')
    btp_cloud_integration_connections: Mapped[List['BtpCloudIntegrationConnections']] = relationship('BtpCloudIntegrationConnections', back_populates='data_source')
    pro_agreements: Mapped[List['ProAgreements']] = relationship('ProAgreements', back_populates='data_source')
    pro_integrated_configurations: Mapped[List['ProIntegratedConfigurations']] = relationship('ProIntegratedConfigurations', back_populates='data_source')


class LeanIxFields(Base):
    __tablename__ = 'lean_ix_fields'
    __table_args__ = (
        ForeignKeyConstraint(['tenant_id'], ['dev.lean_ix_tenants.id'], ondelete='CASCADE', name='lean_ix_fields_lean_ix_tenants_fields'),
        PrimaryKeyConstraint('id', name='lean_ix_fields_pkey'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    tenant_id: Mapped[str] = mapped_column(String)

    tenant: Mapped['LeanIxTenants'] = relationship('LeanIxTenants', foreign_keys=[tenant_id], back_populates='lean_ix_fields')
    lean_ix_tenants: Mapped[List['LeanIxTenants']] = relationship('LeanIxTenants', foreign_keys='[LeanIxTenants.target_field_id]', back_populates='target_field')


class LeanIxTags(Base):
    __tablename__ = 'lean_ix_tags'
    __table_args__ = (
        ForeignKeyConstraint(['tenant_id'], ['dev.lean_ix_tenants.id'], ondelete='CASCADE', name='lean_ix_tags_lean_ix_tenants_tags'),
        PrimaryKeyConstraint('id', name='lean_ix_tags_pkey'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    key: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    tenant_id: Mapped[str] = mapped_column(String)

    tenant: Mapped['LeanIxTenants'] = relationship('LeanIxTenants', foreign_keys=[tenant_id], back_populates='lean_ix_tags')
    lean_ix_tenants: Mapped[List['LeanIxTenants']] = relationship('LeanIxTenants', foreign_keys='[LeanIxTenants.target_tag_id]', back_populates='target_tag')


class LeanIxTenants(Base):
    __tablename__ = 'lean_ix_tenants'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], ondelete='CASCADE', name='lean_ix_tenants_data_sources_leanix_tenant'),
        ForeignKeyConstraint(['property_component_id'], ['dev.property_types.id'], ondelete='SET NULL', name='lean_ix_tenants_property_types_property_component'),
        ForeignKeyConstraint(['property_external_id'], ['dev.property_types.id'], ondelete='SET NULL', name='lean_ix_tenants_property_types_property_external'),
        ForeignKeyConstraint(['target_field_id'], ['dev.lean_ix_fields.id'], ondelete='SET NULL', name='lean_ix_tenants_lean_ix_fields_target_field'),
        ForeignKeyConstraint(['target_tag_id'], ['dev.lean_ix_tags.id'], ondelete='SET NULL', name='lean_ix_tenants_lean_ix_tags_target_tag'),
        PrimaryKeyConstraint('id', name='lean_ix_tenants_pkey'),
        Index('lean_ix_tenants_data_source_id_key', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    data_source_id: Mapped[str] = mapped_column(String)
    overwrite_tags: Mapped[bool] = mapped_column(Boolean, server_default=text('false'))
    has_applications: Mapped[Optional[bool]] = mapped_column(Boolean)
    update_mode: Mapped[Optional[str]] = mapped_column(String)
    target_tag_id: Mapped[Optional[str]] = mapped_column(String)
    target_field_id: Mapped[Optional[str]] = mapped_column(String)
    property_component_id: Mapped[Optional[str]] = mapped_column(String)
    property_external_id: Mapped[Optional[str]] = mapped_column(String)

    lean_ix_fields: Mapped[List['LeanIxFields']] = relationship('LeanIxFields', foreign_keys='[LeanIxFields.tenant_id]', back_populates='tenant')
    lean_ix_tags: Mapped[List['LeanIxTags']] = relationship('LeanIxTags', foreign_keys='[LeanIxTags.tenant_id]', back_populates='tenant')
    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='lean_ix_tenants')
    property_component: Mapped[Optional['PropertyTypes']] = relationship('PropertyTypes', foreign_keys=[property_component_id], back_populates='lean_ix_tenants')
    property_external: Mapped[Optional['PropertyTypes']] = relationship('PropertyTypes', foreign_keys=[property_external_id], back_populates='lean_ix_tenants_')
    target_field: Mapped[Optional['LeanIxFields']] = relationship('LeanIxFields', foreign_keys=[target_field_id], back_populates='lean_ix_tenants')
    target_tag: Mapped[Optional['LeanIxTags']] = relationship('LeanIxTags', foreign_keys=[target_tag_id], back_populates='lean_ix_tenants')


class PropertyTypes(Base):
    __tablename__ = 'property_types'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='property_types_pkey'),
        Index('propertytype_kind_name', 'kind', 'name', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    kind: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)

    lean_ix_tenants: Mapped[List['LeanIxTenants']] = relationship('LeanIxTenants', foreign_keys='[LeanIxTenants.property_component_id]', back_populates='property_component')
    lean_ix_tenants_: Mapped[List['LeanIxTenants']] = relationship('LeanIxTenants', foreign_keys='[LeanIxTenants.property_external_id]', back_populates='property_external')
    btp_tenants: Mapped[List['BtpTenants']] = relationship('BtpTenants', back_populates='property_key')
    hopex_tenants: Mapped[List['HopexTenants']] = relationship('HopexTenants', back_populates='property_external')
    properties: Mapped[List['Properties']] = relationship('Properties', back_populates='type')


class Systems(Base):
    __tablename__ = 'systems'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], ondelete='CASCADE', name='systems_data_sources_system_catalog'),
        PrimaryKeyConstraint('id', name='systems_pkey'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)
    data_source_id: Mapped[Optional[str]] = mapped_column(String)

    data_sources: Mapped[List['DataSources']] = relationship('DataSources', foreign_keys='[DataSources.system_id]', back_populates='system')
    data_source: Mapped[Optional['DataSources']] = relationship('DataSources', foreign_keys=[data_source_id], back_populates='systems')
    data_flows: Mapped[List['DataFlows']] = relationship('DataFlows', foreign_keys='[DataFlows.receiver_id]', back_populates='receiver')
    data_flows_: Mapped[List['DataFlows']] = relationship('DataFlows', foreign_keys='[DataFlows.sender_id]', back_populates='sender')
    inventories: Mapped[List['Inventories']] = relationship('Inventories', foreign_keys='[Inventories.receiver_id]', back_populates='receiver')
    inventories_: Mapped[List['Inventories']] = relationship('Inventories', foreign_keys='[Inventories.sender_id]', back_populates='sender')
    system_mappings: Mapped[List['SystemMappings']] = relationship('SystemMappings', back_populates='target_system')
    metadata_: Mapped[List['Metadata']] = relationship('Metadata', back_populates='system')
    properties: Mapped[List['Properties']] = relationship('Properties', back_populates='system')


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='users_pkey'),
        Index('user_email', 'email', unique=True),
        Index('user_email_active', 'email', 'active'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    active: Mapped[bool] = mapped_column(Boolean)
    role: Mapped[str] = mapped_column(String, server_default=text("'U'::character varying"))

    sessions: Mapped[List['Sessions']] = relationship('Sessions', back_populates='user')
    user_sessions: Mapped[List['UserSessions']] = relationship('UserSessions', back_populates='user')


class AbapOdataServices(Base):
    __tablename__ = 'abap_odata_services'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='abap_odata_services_data_sources_data_source'),
        PrimaryKeyConstraint('id', name='abap_odata_services_pkey'),
        Index('abapodataservice_name_data_source_id', 'name', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    version: Mapped[int] = mapped_column(BigInteger)
    url: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)
    created_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    created_by: Mapped[Optional[str]] = mapped_column(String)
    changed_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    changed_by: Mapped[Optional[str]] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='abap_odata_services')


class AbapPartnerProfiles(Base):
    __tablename__ = 'abap_partner_profiles'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='abap_partner_profiles_data_sources_data_source'),
        PrimaryKeyConstraint('id', name='abap_partner_profiles_pkey'),
        Index('abappartnerprofile_name_type_d_7ce8142de5f3f317b8727b33a628c7c6', 'name', 'type', 'direction', 'function', 'message_type', 'message_code', 'message_function', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    direction: Mapped[str] = mapped_column(String)
    message_type: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)
    function: Mapped[Optional[str]] = mapped_column(String)
    message_code: Mapped[Optional[str]] = mapped_column(String)
    message_function: Mapped[Optional[str]] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='abap_partner_profiles')
    abap_inbound_partner_profiles: Mapped[List['AbapInboundPartnerProfiles']] = relationship('AbapInboundPartnerProfiles', back_populates='profile')
    abap_outbound_partner_profiles: Mapped[List['AbapOutboundPartnerProfiles']] = relationship('AbapOutboundPartnerProfiles', back_populates='profile')


class AbapPaths(Base):
    __tablename__ = 'abap_paths'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='abap_paths_data_sources_data_source'),
        PrimaryKeyConstraint('id', name='abap_paths_pkey'),
        Index('abappath_name_type_data_source_id', 'name', 'type', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    path: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='abap_paths')


class AbapRfcDestinations(Base):
    __tablename__ = 'abap_rfc_destinations'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='abap_rfc_destinations_data_sources_data_source'),
        PrimaryKeyConstraint('id', name='abap_rfc_destinations_pkey'),
        Index('abaprfcdestination_name_type_data_source_id', 'name', 'type', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)
    created_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    created_by: Mapped[Optional[str]] = mapped_column(String)
    changed_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    changed_by: Mapped[Optional[str]] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='abap_rfc_destinations')
    abap_integration_engine_interfaces: Mapped[List['AbapIntegrationEngineInterfaces']] = relationship('AbapIntegrationEngineInterfaces', back_populates='abap_rfc_destinations')
    abap_ports: Mapped[List['AbapPorts']] = relationship('AbapPorts', back_populates='abap_rfc_destinations')
    abap_qrfc_destinations: Mapped[List['AbapQrfcDestinations']] = relationship('AbapQrfcDestinations', back_populates='destination')
    abap_rfc_destination_options: Mapped[List['AbapRfcDestinationOptions']] = relationship('AbapRfcDestinationOptions', back_populates='destination')


class AbapSoapServices(Base):
    __tablename__ = 'abap_soap_services'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='abap_soap_services_data_sources_data_source'),
        PrimaryKeyConstraint('id', name='abap_soap_services_pkey'),
        Index('abapsoapservice_key_data_source_id', 'key', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    key: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    object: Mapped[str] = mapped_column(String)
    state: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    sc: Mapped[bool] = mapped_column(Boolean)
    data_source_id: Mapped[str] = mapped_column(String)
    created_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    created_by: Mapped[Optional[str]] = mapped_column(String)
    changed_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    changed_by: Mapped[Optional[str]] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='abap_soap_services')
    abap_soap_service_bindings: Mapped[List['AbapSoapServiceBindings']] = relationship('AbapSoapServiceBindings', back_populates='service')


class AbapSystems(Base):
    __tablename__ = 'abap_systems'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], ondelete='CASCADE', name='abap_systems_data_sources_abap_system'),
        PrimaryKeyConstraint('id', name='abap_systems_pkey'),
        Index('abap_systems_data_source_id_key', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    type: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)
    system_no: Mapped[Optional[str]] = mapped_column(String)
    client_no: Mapped[Optional[str]] = mapped_column(String)
    router: Mapped[Optional[str]] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='abap_systems')


class AnypointAssets(Base):
    __tablename__ = 'anypoint_assets'
    __table_args__ = (
        ForeignKeyConstraint(['organisation_id'], ['dev.anypoint_organisations.id'], ondelete='CASCADE', name='anypoint_assets_anypoint_organisations_assets'),
        PrimaryKeyConstraint('id', name='anypoint_assets_pkey'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    version: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    organisation_id: Mapped[str] = mapped_column(String)
    created_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    created_by: Mapped[Optional[str]] = mapped_column(String)
    changed_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    changed_by: Mapped[Optional[str]] = mapped_column(String)

    organisation: Mapped['AnypointOrganisations'] = relationship('AnypointOrganisations', back_populates='anypoint_assets')


class AzureTenants(Base):
    __tablename__ = 'azure_tenants'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], ondelete='CASCADE', name='azure_tenants_data_sources_azure_tenant'),
        PrimaryKeyConstraint('id', name='azure_tenants_pkey'),
        Index('azure_tenants_data_source_id_key', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)
    has_api_management: Mapped[Optional[bool]] = mapped_column(Boolean)
    has_event_grid: Mapped[Optional[bool]] = mapped_column(Boolean)
    has_logic_apps: Mapped[Optional[bool]] = mapped_column(Boolean)
    has_standard_apps: Mapped[Optional[bool]] = mapped_column(Boolean)
    has_service_bus: Mapped[Optional[bool]] = mapped_column(Boolean)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='azure_tenants')
    azure_subscriptions: Mapped[List['AzureSubscriptions']] = relationship('AzureSubscriptions', back_populates='tenant')


class BtpApiManagementProducts(Base):
    __tablename__ = 'btp_api_management_products'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='btp_api_management_products_data_sources_data_source'),
        PrimaryKeyConstraint('id', name='btp_api_management_products_pkey'),
        Index('btpapimanagementproduct_name_data_source_id', 'name', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    version: Mapped[str] = mapped_column(String)
    scope: Mapped[str] = mapped_column(String)
    quota_count: Mapped[int] = mapped_column(BigInteger)
    quota_interval: Mapped[int] = mapped_column(BigInteger)
    quota_unit: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)
    created_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    created_by: Mapped[Optional[str]] = mapped_column(String)
    changed_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    changed_by: Mapped[Optional[str]] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='btp_api_management_products')
    btp_api_management_proxy: Mapped[List['BtpApiManagementProxies']] = relationship('BtpApiManagementProxies', secondary='dev.btp_api_management_proxy_products', back_populates='btp_api_management_product')
    btp_api_management_product_applications: Mapped[List['BtpApiManagementProductApplications']] = relationship('BtpApiManagementProductApplications', back_populates='product')
    btp_api_management_product_rate_plans: Mapped[List['BtpApiManagementProductRatePlans']] = relationship('BtpApiManagementProductRatePlans', back_populates='product')


class BtpApiManagementProviders(Base):
    __tablename__ = 'btp_api_management_providers'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='btp_api_management_providers_data_sources_data_source'),
        PrimaryKeyConstraint('id', name='btp_api_management_providers_pkey'),
        Index('btpapimanagementprovider_name_data_source_id', 'name', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    url: Mapped[str] = mapped_column(String)
    host: Mapped[str] = mapped_column(String)
    port: Mapped[str] = mapped_column(String)
    use_ssl: Mapped[bool] = mapped_column(Boolean)
    authentication: Mapped[str] = mapped_column(String)
    region: Mapped[str] = mapped_column(String)
    location_id: Mapped[str] = mapped_column(String)
    sap_client_id: Mapped[str] = mapped_column(String)
    path_prefix: Mapped[str] = mapped_column(String)
    cockpit_url: Mapped[str] = mapped_column(String)
    authentication_type: Mapped[str] = mapped_column(String)
    authentication_username: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)
    created_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    created_by: Mapped[Optional[str]] = mapped_column(String)
    changed_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    changed_by: Mapped[Optional[str]] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='btp_api_management_providers')
    btp_api_management_proxies: Mapped[List['BtpApiManagementProxies']] = relationship('BtpApiManagementProxies', back_populates='provider')


class BtpCloudIntegrationCredentials(Base):
    __tablename__ = 'btp_cloud_integration_credentials'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], ondelete='CASCADE', name='btp_cloud_integration_credentials_data_sources_data_source'),
        PrimaryKeyConstraint('id', name='btp_cloud_integration_credentials_pkey'),
        Index('btpcloudintegrationcredentials_name_data_source_id', 'name', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    ident: Mapped[str] = mapped_column(String)
    deployed_on: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    deployed_by: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='btp_cloud_integration_credentials')
    btp_cloud_integration_oauth2credentials: Mapped[List['BtpCloudIntegrationOauth2credentials']] = relationship('BtpCloudIntegrationOauth2credentials', back_populates='credential')
    btp_cloud_integration_connections: Mapped[List['BtpCloudIntegrationConnections']] = relationship('BtpCloudIntegrationConnections', back_populates='credential')


class BtpCloudIntegrationMessages(Base):
    __tablename__ = 'btp_cloud_integration_messages'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='btp_cloud_integration_messages_data_sources_data_source'),
        PrimaryKeyConstraint('id', name='btp_cloud_integration_messages_pkey'),
        Index('btpcloudintegrationmessage_message_data_source_id', 'message', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    message: Mapped[str] = mapped_column(String)
    correlation: Mapped[str] = mapped_column(String)
    started_on: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    finished_on: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    status: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)
    package: Mapped[Optional[str]] = mapped_column(String)
    artefact: Mapped[Optional[str]] = mapped_column(String)
    sender: Mapped[Optional[str]] = mapped_column(String)
    receiver: Mapped[Optional[str]] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='btp_cloud_integration_messages')
    btp_cloud_integration_message_attachments: Mapped[List['BtpCloudIntegrationMessageAttachments']] = relationship('BtpCloudIntegrationMessageAttachments', back_populates='message')
    btp_cloud_integration_message_properties: Mapped[List['BtpCloudIntegrationMessageProperties']] = relationship('BtpCloudIntegrationMessageProperties', back_populates='message')
    btp_cloud_integration_message_store_entries: Mapped[List['BtpCloudIntegrationMessageStoreEntries']] = relationship('BtpCloudIntegrationMessageStoreEntries', back_populates='message')


class BtpCloudIntegrationPackages(Base):
    __tablename__ = 'btp_cloud_integration_packages'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='btp_cloud_integration_packages_data_sources_data_source'),
        PrimaryKeyConstraint('id', name='btp_cloud_integration_packages_pkey'),
        Index('btpcloudintegrationpackage_key_data_source_id', 'key', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    key: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    version: Mapped[str] = mapped_column(String)
    update_available: Mapped[bool] = mapped_column(Boolean)
    data_source_id: Mapped[str] = mapped_column(String)
    created_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    created_by: Mapped[Optional[str]] = mapped_column(String)
    changed_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    changed_by: Mapped[Optional[str]] = mapped_column(String)
    short_text: Mapped[Optional[str]] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)
    vendor: Mapped[Optional[str]] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='btp_cloud_integration_packages')
    btp_cloud_integration_artefacts: Mapped[List['BtpCloudIntegrationArtefacts']] = relationship('BtpCloudIntegrationArtefacts', back_populates='package')
    btp_cloud_integration_package_tags: Mapped[List['BtpCloudIntegrationPackageTags']] = relationship('BtpCloudIntegrationPackageTags', back_populates='package')


class BtpCloudIntegrationRuntimeArtefacts(Base):
    __tablename__ = 'btp_cloud_integration_runtime_artefacts'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], ondelete='CASCADE', name='btp_cloud_integration_runtime__f055acd898a6b157ff51c7c38cfe3d75'),
        PrimaryKeyConstraint('id', name='btp_cloud_integration_runtime_artefacts_pkey'),
        Index('btpcloudintegrationruntimeartefact_key_version_data_source_id', 'key', 'version', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    key: Mapped[str] = mapped_column(String)
    version: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    deployed_on: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    deployed_by: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='btp_cloud_integration_runtime_artefacts')
    btp_cloud_integration_artefacts: Mapped[List['BtpCloudIntegrationArtefacts']] = relationship('BtpCloudIntegrationArtefacts', back_populates='runtime')
    btp_cloud_integration_service_endpoints: Mapped[List['BtpCloudIntegrationServiceEndpoints']] = relationship('BtpCloudIntegrationServiceEndpoints', back_populates='runtime')


class BtpEventMeshQueues(Base):
    __tablename__ = 'btp_event_mesh_queues'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='btp_event_mesh_queues_data_sources_data_source'),
        PrimaryKeyConstraint('id', name='btp_event_mesh_queues_pkey'),
        Index('btpeventmeshqueue_name_data_source_id', 'name', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    access_type: Mapped[str] = mapped_column(String)
    message_count: Mapped[int] = mapped_column(BigInteger)
    unacknowledged_message_count: Mapped[int] = mapped_column(BigInteger)
    queue_size_in_bytes: Mapped[int] = mapped_column(BigInteger)
    max_queue_size_in_bytes: Mapped[int] = mapped_column(BigInteger)
    max_message_size_in_bytes: Mapped[int] = mapped_column(BigInteger)
    max_unacknowledged_messages: Mapped[int] = mapped_column(BigInteger)
    max_redelivery_count: Mapped[int] = mapped_column(BigInteger)
    max_time_to_live: Mapped[int] = mapped_column(BigInteger)
    dead_message_queue: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='btp_event_mesh_queues')
    btp_event_mesh_topic: Mapped[List['BtpEventMeshTopics']] = relationship('BtpEventMeshTopics', secondary='dev.btp_event_mesh_queue_topics', back_populates='btp_event_mesh_queue')
    btp_event_mesh_webhooks: Mapped[List['BtpEventMeshWebhooks']] = relationship('BtpEventMeshWebhooks', back_populates='btp_event_mesh_queues')


class BtpEventMeshTopics(Base):
    __tablename__ = 'btp_event_mesh_topics'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='btp_event_mesh_topics_data_sources_data_source'),
        PrimaryKeyConstraint('id', name='btp_event_mesh_topics_pkey'),
        Index('btpeventmeshtopic_name_data_source_id', 'name', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)

    btp_event_mesh_queue: Mapped[List['BtpEventMeshQueues']] = relationship('BtpEventMeshQueues', secondary='dev.btp_event_mesh_queue_topics', back_populates='btp_event_mesh_topic')
    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='btp_event_mesh_topics')


class BtpTenants(Base):
    __tablename__ = 'btp_tenants'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], ondelete='CASCADE', name='btp_tenants_data_sources_btp_tenant'),
        ForeignKeyConstraint(['property_key_id'], ['dev.property_types.id'], ondelete='SET NULL', name='btp_tenants_property_types_property_key'),
        PrimaryKeyConstraint('id', name='btp_tenants_pkey'),
        Index('btp_tenants_data_source_id_key', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    product: Mapped[str] = mapped_column(String)
    region: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)
    property_key_id: Mapped[Optional[str]] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='btp_tenants')
    property_key: Mapped[Optional['PropertyTypes']] = relationship('PropertyTypes', back_populates='btp_tenants')


class DataFlows(Base):
    __tablename__ = 'data_flows'
    __table_args__ = (
        ForeignKeyConstraint(['receiver_id'], ['dev.systems.id'], ondelete='SET NULL', name='data_flows_systems_receiver'),
        ForeignKeyConstraint(['sender_id'], ['dev.systems.id'], ondelete='SET NULL', name='data_flows_systems_sender'),
        PrimaryKeyConstraint('id', name='data_flows_pkey'),
        Index('dataflow_name', 'name', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)
    sender_id: Mapped[Optional[str]] = mapped_column(String)
    receiver_id: Mapped[Optional[str]] = mapped_column(String)

    receiver: Mapped[Optional['Systems']] = relationship('Systems', foreign_keys=[receiver_id], back_populates='data_flows')
    sender: Mapped[Optional['Systems']] = relationship('Systems', foreign_keys=[sender_id], back_populates='data_flows_')
    data_flow_items: Mapped[List['DataFlowItems']] = relationship('DataFlowItems', back_populates='data_flow')
    properties: Mapped[List['Properties']] = relationship('Properties', back_populates='data_flow')


class DataSourceAccessTokens(Base):
    __tablename__ = 'data_source_access_tokens'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], ondelete='CASCADE', name='data_source_access_tokens_data_sources_access_tokens'),
        PrimaryKeyConstraint('id', name='data_source_access_tokens_pkey'),
        Index('datasourceaccesstoken_token_valid_to', 'token', 'valid_to', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    token: Mapped[str] = mapped_column(String)
    valid_to: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    data_source_id: Mapped[str] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='data_source_access_tokens')


class DataSourceApiKeys(Base):
    __tablename__ = 'data_source_api_keys'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], ondelete='CASCADE', name='data_source_api_keys_data_sources_api_key'),
        PrimaryKeyConstraint('id', name='data_source_api_keys_pkey'),
        Index('data_source_api_keys_data_source_id_key', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    header: Mapped[str] = mapped_column(String)
    key: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='data_source_api_keys')


class DataSourceBasicAuthCredentials(Base):
    __tablename__ = 'data_source_basic_auth_credentials'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], ondelete='CASCADE', name='data_source_basic_auth_credent_9bc01ab746f84199d6a9cefd45c496ca'),
        ForeignKeyConstraint(['proxy_id'], ['dev.data_source_proxies.id'], ondelete='CASCADE', name='data_source_basic_auth_credent_90e88c39ab9caf141b101c09ded89d31'),
        PrimaryKeyConstraint('id', name='data_source_basic_auth_credentials_pkey'),
        Index('data_source_basic_auth_credentials_data_source_id_key', 'data_source_id', unique=True),
        Index('data_source_basic_auth_credentials_proxy_id_key', 'proxy_id', unique=True),
        Index('datasourcebasicauthcredentials_username', 'username', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    username: Mapped[bytes] = mapped_column(LargeBinary)
    password: Mapped[bytes] = mapped_column(LargeBinary)
    data_source_id: Mapped[Optional[str]] = mapped_column(String)
    proxy_id: Mapped[Optional[str]] = mapped_column(String)

    data_source: Mapped[Optional['DataSources']] = relationship('DataSources', back_populates='data_source_basic_auth_credentials')
    proxy: Mapped[Optional['DataSourceProxies']] = relationship('DataSourceProxies', back_populates='data_source_basic_auth_credentials')


class DataSourceOauth2credentials(Base):
    __tablename__ = 'data_source_oauth2credentials'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], ondelete='CASCADE', name='data_source_oauth2credentials_data_sources_oauth2_credentials'),
        ForeignKeyConstraint(['proxy_id'], ['dev.data_source_proxies.id'], ondelete='CASCADE', name='data_source_oauth2credentials__d6767fce8393abb692a0b46fe5da92a6'),
        PrimaryKeyConstraint('id', name='data_source_oauth2credentials_pkey'),
        Index('data_source_oauth2credentials_data_source_id_key', 'data_source_id', unique=True),
        Index('data_source_oauth2credentials_proxy_id_key', 'proxy_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    client_id: Mapped[str] = mapped_column(String)
    secret: Mapped[bytes] = mapped_column(LargeBinary)
    scope: Mapped[str] = mapped_column(String)
    token_url: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[Optional[str]] = mapped_column(String)
    proxy_id: Mapped[Optional[str]] = mapped_column(String)

    data_source: Mapped[Optional['DataSources']] = relationship('DataSources', back_populates='data_source_oauth2credentials')
    proxy: Mapped[Optional['DataSourceProxies']] = relationship('DataSourceProxies', back_populates='data_source_oauth2credentials')


class DataSourceProxyHeaders(Base):
    __tablename__ = 'data_source_proxy_headers'
    __table_args__ = (
        ForeignKeyConstraint(['proxy_id'], ['dev.data_source_proxies.id'], ondelete='CASCADE', name='data_source_proxy_headers_data_source_proxies_headers'),
        PrimaryKeyConstraint('id', name='data_source_proxy_headers_pkey'),
        Index('datasourceproxyheader_name', 'name', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    value: Mapped[str] = mapped_column(String)
    proxy_id: Mapped[str] = mapped_column(String)

    proxy: Mapped['DataSourceProxies'] = relationship('DataSourceProxies', back_populates='data_source_proxy_headers')


class HopexTenants(Base):
    __tablename__ = 'hopex_tenants'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], ondelete='CASCADE', name='hopex_tenants_data_sources_hopex_tenant'),
        ForeignKeyConstraint(['property_external_id'], ['dev.property_types.id'], ondelete='SET NULL', name='hopex_tenants_property_types_property_external'),
        PrimaryKeyConstraint('id', name='hopex_tenants_pkey'),
        Index('hopex_tenants_data_source_id_key', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    data_source_id: Mapped[str] = mapped_column(String)
    update_mode: Mapped[Optional[str]] = mapped_column(String)
    property_external_id: Mapped[Optional[str]] = mapped_column(String)
    has_applications: Mapped[Optional[bool]] = mapped_column(Boolean)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='hopex_tenants')
    property_external: Mapped[Optional['PropertyTypes']] = relationship('PropertyTypes', back_populates='hopex_tenants')


class Inventories(Base):
    __tablename__ = 'inventories'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], ondelete='CASCADE', name='inventories_data_sources_inventory'),
        ForeignKeyConstraint(['receiver_id'], ['dev.systems.id'], ondelete='SET NULL', name='inventories_systems_receiver'),
        ForeignKeyConstraint(['sender_id'], ['dev.systems.id'], ondelete='SET NULL', name='inventories_systems_sender'),
        PrimaryKeyConstraint('id', name='inventories_pkey'),
        Index('inventory_object_id', 'object_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    vendor: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)
    object_id: Mapped[Optional[str]] = mapped_column(String)
    object_url: Mapped[Optional[str]] = mapped_column(String)
    object_args: Mapped[Optional[str]] = mapped_column(String)
    sender_name: Mapped[Optional[str]] = mapped_column(String)
    receiver_name: Mapped[Optional[str]] = mapped_column(String)
    data_source_id: Mapped[Optional[str]] = mapped_column(String)
    sender_id: Mapped[Optional[str]] = mapped_column(String)
    receiver_id: Mapped[Optional[str]] = mapped_column(String)

    data_source: Mapped[Optional['DataSources']] = relationship('DataSources', back_populates='inventories')
    receiver: Mapped[Optional['Systems']] = relationship('Systems', foreign_keys=[receiver_id], back_populates='inventories')
    sender: Mapped[Optional['Systems']] = relationship('Systems', foreign_keys=[sender_id], back_populates='inventories_')
    data_flow_items: Mapped[List['DataFlowItems']] = relationship('DataFlowItems', back_populates='inventory')
    metadata_: Mapped[List['Metadata']] = relationship('Metadata', back_populates='inventory')
    properties: Mapped[List['Properties']] = relationship('Properties', back_populates='inventory')


class LuyTenants(Base):
    __tablename__ = 'luy_tenants'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], ondelete='CASCADE', name='luy_tenants_data_sources_luy_tenant'),
        PrimaryKeyConstraint('id', name='luy_tenants_pkey'),
        Index('luy_tenants_data_source_id_key', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    data_source_id: Mapped[str] = mapped_column(String)
    has_information_systems: Mapped[Optional[bool]] = mapped_column(Boolean)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='luy_tenants')


class ProCommunicationParties(Base):
    __tablename__ = 'pro_communication_parties'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='pro_communication_parties_data_sources_data_source'),
        PrimaryKeyConstraint('id', name='pro_communication_parties_pkey'),
        Index('procommunicationparty_name_data_source_id', 'name', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    responsible: Mapped[str] = mapped_column(String)
    changed_on: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    changed_by: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)
    folder: Mapped[Optional[str]] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='pro_communication_parties')
    pro_configuration_scenario: Mapped[List['ProConfigurationScenarios']] = relationship('ProConfigurationScenarios', secondary='dev.pro_configuration_scenario_parties', back_populates='pro_communication_party')
    pro_communication_components: Mapped[List['ProCommunicationComponents']] = relationship('ProCommunicationComponents', back_populates='pro_communication_parties')
    pro_communication_channels: Mapped[List['ProCommunicationChannels']] = relationship('ProCommunicationChannels', back_populates='party')


class ProConfigurationScenarios(Base):
    __tablename__ = 'pro_configuration_scenarios'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='pro_configuration_scenarios_data_sources_data_source'),
        PrimaryKeyConstraint('id', name='pro_configuration_scenarios_pkey'),
        Index('proconfigurationscenario_name_data_source_id', 'name', 'data_source_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    responsible: Mapped[str] = mapped_column(String)
    changed_on: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    changed_by: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)
    folder: Mapped[Optional[str]] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)

    pro_communication_party: Mapped[List['ProCommunicationParties']] = relationship('ProCommunicationParties', secondary='dev.pro_configuration_scenario_parties', back_populates='pro_configuration_scenario')
    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='pro_configuration_scenarios')
    pro_integrated_configuration: Mapped[List['ProIntegratedConfigurations']] = relationship('ProIntegratedConfigurations', secondary='dev.pro_configuration_scenario_configurations', back_populates='pro_configuration_scenario')
    pro_communication_component: Mapped[List['ProCommunicationComponents']] = relationship('ProCommunicationComponents', secondary='dev.pro_configuration_scenario_components', back_populates='pro_configuration_scenario')
    pro_communication_channel: Mapped[List['ProCommunicationChannels']] = relationship('ProCommunicationChannels', secondary='dev.pro_configuration_scenario_channels', back_populates='pro_configuration_scenario')
    pro_agreement: Mapped[List['ProAgreements']] = relationship('ProAgreements', secondary='dev.pro_configuration_scenario_receiver_agreements', back_populates='pro_configuration_scenario')
    pro_agreement_: Mapped[List['ProAgreements']] = relationship('ProAgreements', secondary='dev.pro_configuration_scenario_sender_agreements', back_populates='pro_configuration_scenario_')


class ProPerformanceQueries(Base):
    __tablename__ = 'pro_performance_queries'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='pro_performance_queries_data_sources_data_source'),
        PrimaryKeyConstraint('id', name='pro_performance_queries_pkey'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    component: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    start_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    end_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    data_source_id: Mapped[str] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='pro_performance_queries')
    pro_performance_data: Mapped[List['ProPerformanceData']] = relationship('ProPerformanceData', back_populates='query')


class ProPerformanceStats(Base):
    __tablename__ = 'pro_performance_stats'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='pro_performance_stats_data_sources_data_source'),
        PrimaryKeyConstraint('id', name='pro_performance_stats_pkey'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    interval: Mapped[str] = mapped_column(String)
    period: Mapped[str] = mapped_column(String)
    sender_party: Mapped[str] = mapped_column(String)
    sender_service: Mapped[str] = mapped_column(String)
    receiver_party: Mapped[str] = mapped_column(String)
    receiver_service: Mapped[str] = mapped_column(String)
    interface_name: Mapped[str] = mapped_column(String)
    namespace: Mapped[str] = mapped_column(String)
    direction: Mapped[str] = mapped_column(String)
    qos: Mapped[str] = mapped_column(String)
    count: Mapped[int] = mapped_column(BigInteger)
    volume: Mapped[int] = mapped_column(BigInteger)
    min_size: Mapped[int] = mapped_column(BigInteger)
    max_size: Mapped[int] = mapped_column(BigInteger)
    avg_size: Mapped[int] = mapped_column(BigInteger)
    avg_runtime: Mapped[float] = mapped_column(REAL)
    min_mapping: Mapped[float] = mapped_column(REAL)
    avg_mapping: Mapped[float] = mapped_column(REAL)
    data_source_id: Mapped[str] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='pro_performance_stats')


class ProSoftwareComponents(Base):
    __tablename__ = 'pro_software_components'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='pro_software_components_data_sources_data_source'),
        PrimaryKeyConstraint('id', name='pro_software_components_pkey'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    version: Mapped[str] = mapped_column(String)
    vendor: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='pro_software_components')


class Sessions(Base):
    __tablename__ = 'sessions'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['dev.users.id'], ondelete='CASCADE', name='sessions_users_sessions'),
        PrimaryKeyConstraint('id', name='sessions_pkey'),
        Index('session_token', 'token', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    provider: Mapped[str] = mapped_column(String)
    state: Mapped[str] = mapped_column(String)
    token: Mapped[str] = mapped_column(String)
    remote_addr: Mapped[str] = mapped_column(String)
    user_agent: Mapped[str] = mapped_column(String)
    data: Mapped[str] = mapped_column(String)
    expires_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    user_id: Mapped[Optional[str]] = mapped_column(String)

    user: Mapped[Optional['Users']] = relationship('Users', back_populates='sessions')


class SystemMappings(Base):
    __tablename__ = 'system_mappings'
    __table_args__ = (
        ForeignKeyConstraint(['target_system_id'], ['dev.systems.id'], ondelete='SET NULL', name='system_mappings_systems_system'),
        PrimaryKeyConstraint('id', name='system_mappings_pkey'),
        Index('systemmapping_interface_pattern_source_system_pattern', 'interface_pattern', 'source_system_pattern', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    source_system_pattern: Mapped[str] = mapped_column(String)
    interface_pattern: Mapped[Optional[str]] = mapped_column(String)
    target_system_id: Mapped[Optional[str]] = mapped_column(String)

    target_system: Mapped[Optional['Systems']] = relationship('Systems', back_populates='system_mappings')


class Tasks(Base):
    __tablename__ = 'tasks'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], ondelete='CASCADE', name='tasks_data_sources_tasks'),
        PrimaryKeyConstraint('id', name='tasks_pkey'),
        Index('task_type_data_source_id', 'type', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    type: Mapped[str] = mapped_column(String)
    start_date: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    unit: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)
    recurrence: Mapped[Optional[int]] = mapped_column(BigInteger)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='tasks')
    task_runs: Mapped[List['TaskRuns']] = relationship('TaskRuns', back_populates='task')


class UserSessions(Base):
    __tablename__ = 'user_sessions'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['dev.users.id'], ondelete='CASCADE', name='user_sessions_users_sessions'),
        PrimaryKeyConstraint('id', name='user_sessions_pkey'),
        Index('usersession_token', 'token', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    provider: Mapped[str] = mapped_column(String)
    state: Mapped[str] = mapped_column(String)
    token: Mapped[str] = mapped_column(String)
    remote_addr: Mapped[str] = mapped_column(String)
    user_agent: Mapped[str] = mapped_column(String)
    data: Mapped[str] = mapped_column(String)
    expires_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    user_id: Mapped[Optional[str]] = mapped_column(String)

    user: Mapped[Optional['Users']] = relationship('Users', back_populates='user_sessions')


class AbapInboundPartnerProfiles(Base):
    __tablename__ = 'abap_inbound_partner_profiles'
    __table_args__ = (
        ForeignKeyConstraint(['profile_id'], ['dev.abap_partner_profiles.id'], ondelete='CASCADE', name='abap_inbound_partner_profiles_abap_partner_profiles_inbound'),
        PrimaryKeyConstraint('id', name='abap_inbound_partner_profiles_pkey'),
        Index('abap_inbound_partner_profiles_profile_id_key', 'profile_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    processing_mode: Mapped[str] = mapped_column(String)
    processing_code: Mapped[str] = mapped_column(String)
    profile_id: Mapped[str] = mapped_column(String)

    profile: Mapped['AbapPartnerProfiles'] = relationship('AbapPartnerProfiles', back_populates='abap_inbound_partner_profiles')


class AbapIntegrationEngineInterfaces(Base):
    __tablename__ = 'abap_integration_engine_interfaces'
    __table_args__ = (
        ForeignKeyConstraint(['abap_integration_engine_interface_destination'], ['dev.abap_rfc_destinations.id'], ondelete='SET NULL', name='abap_integration_engine_interf_0b5df6ef06350d8b06bf1356d3b1e6ad'),
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='abap_integration_engine_interfaces_data_sources_data_source'),
        PrimaryKeyConstraint('id', name='abap_integration_engine_interfaces_pkey'),
        Index('abapintegrationengineinterface_name_data_source_id', 'name', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    party: Mapped[str] = mapped_column(String)
    service: Mapped[str] = mapped_column(String)
    action: Mapped[str] = mapped_column(String)
    namespace: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)
    created_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    created_by: Mapped[Optional[str]] = mapped_column(String)
    changed_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    changed_by: Mapped[Optional[str]] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)
    abap_integration_engine_interface_destination: Mapped[Optional[str]] = mapped_column(String)

    abap_rfc_destinations: Mapped[Optional['AbapRfcDestinations']] = relationship('AbapRfcDestinations', back_populates='abap_integration_engine_interfaces')
    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='abap_integration_engine_interfaces')


class AbapPorts(Base):
    __tablename__ = 'abap_ports'
    __table_args__ = (
        ForeignKeyConstraint(['abap_port_destination'], ['dev.abap_rfc_destinations.id'], name='abap_ports_abap_rfc_destinations_destination'),
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='abap_ports_data_sources_data_source'),
        PrimaryKeyConstraint('id', name='abap_ports_pkey'),
        Index('abapport_name_type_data_source_id', 'name', 'type', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)
    abap_port_destination: Mapped[str] = mapped_column(String)

    abap_rfc_destinations: Mapped['AbapRfcDestinations'] = relationship('AbapRfcDestinations', back_populates='abap_ports')
    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='abap_ports')
    abap_outbound_partner_profiles: Mapped[List['AbapOutboundPartnerProfiles']] = relationship('AbapOutboundPartnerProfiles', back_populates='abap_ports')


class AbapQrfcDestinations(Base):
    __tablename__ = 'abap_qrfc_destinations'
    __table_args__ = (
        ForeignKeyConstraint(['destination_id'], ['dev.abap_rfc_destinations.id'], ondelete='CASCADE', name='abap_qrfc_destinations_abap_rfc_destinations_qrfc'),
        PrimaryKeyConstraint('id', name='abap_qrfc_destinations_pkey'),
        Index('abap_qrfc_destinations_destination_id_key', 'destination_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    state: Mapped[str] = mapped_column(String)
    max_connections: Mapped[str] = mapped_column(String)
    timeout: Mapped[str] = mapped_column(String)
    hostname: Mapped[str] = mapped_column(String)
    destination_id: Mapped[str] = mapped_column(String)

    destination: Mapped['AbapRfcDestinations'] = relationship('AbapRfcDestinations', back_populates='abap_qrfc_destinations')


class AbapRfcDestinationOptions(Base):
    __tablename__ = 'abap_rfc_destination_options'
    __table_args__ = (
        ForeignKeyConstraint(['destination_id'], ['dev.abap_rfc_destinations.id'], name='abap_rfc_destination_options_abap_rfc_destinations_options'),
        PrimaryKeyConstraint('id', name='abap_rfc_destination_options_pkey'),
        Index('abaprfcdestinationoption_key_destination_id', 'key', 'destination_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    key: Mapped[str] = mapped_column(String)
    value: Mapped[str] = mapped_column(String)
    destination_id: Mapped[str] = mapped_column(String)

    destination: Mapped['AbapRfcDestinations'] = relationship('AbapRfcDestinations', back_populates='abap_rfc_destination_options')


class AbapSoapServiceBindings(Base):
    __tablename__ = 'abap_soap_service_bindings'
    __table_args__ = (
        ForeignKeyConstraint(['service_id'], ['dev.abap_soap_services.id'], name='abap_soap_service_bindings_abap_soap_services_bindings'),
        PrimaryKeyConstraint('id', name='abap_soap_service_bindings_pkey'),
        Index('abapsoapservicebinding_name_service_id', 'name', 'service_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    service_id: Mapped[str] = mapped_column(String)

    service: Mapped['AbapSoapServices'] = relationship('AbapSoapServices', back_populates='abap_soap_service_bindings')
    abap_soap_service_binding_properties: Mapped[List['AbapSoapServiceBindingProperties']] = relationship('AbapSoapServiceBindingProperties', back_populates='binding')


class AzureSubscriptions(Base):
    __tablename__ = 'azure_subscriptions'
    __table_args__ = (
        ForeignKeyConstraint(['tenant_id'], ['dev.azure_tenants.id'], name='azure_subscriptions_azure_tenants_subscriptions'),
        PrimaryKeyConstraint('id', name='azure_subscriptions_pkey'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(Text)
    tenant_id: Mapped[str] = mapped_column(String)

    tenant: Mapped['AzureTenants'] = relationship('AzureTenants', back_populates='azure_subscriptions')
    azure_resource_groups: Mapped[List['AzureResourceGroups']] = relationship('AzureResourceGroups', back_populates='subscription')


class BtpApiManagementProductApplications(Base):
    __tablename__ = 'btp_api_management_product_applications'
    __table_args__ = (
        ForeignKeyConstraint(['product_id'], ['dev.btp_api_management_products.id'], ondelete='CASCADE', name='btp_api_management_product_app_c4e07db1b3991c1f76e109ae3b79c738'),
        PrimaryKeyConstraint('id', name='btp_api_management_product_applications_pkey'),
        Index('btpapimanagementproductapplication_title_product_id', 'title', 'product_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    title: Mapped[str] = mapped_column(String)
    product_id: Mapped[str] = mapped_column(String)

    product: Mapped['BtpApiManagementProducts'] = relationship('BtpApiManagementProducts', back_populates='btp_api_management_product_applications')


class BtpApiManagementProductRatePlans(Base):
    __tablename__ = 'btp_api_management_product_rate_plans'
    __table_args__ = (
        ForeignKeyConstraint(['product_id'], ['dev.btp_api_management_products.id'], ondelete='CASCADE', name='btp_api_management_product_rat_b674101ba4be9c9d446d5a677402f52b'),
        PrimaryKeyConstraint('id', name='btp_api_management_product_rate_plans_pkey'),
        Index('btpapimanagementproductrateplan_name_product_id', 'name', 'product_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    frequency: Mapped[str] = mapped_column(String)
    currency: Mapped[str] = mapped_column(String)
    plan_type: Mapped[str] = mapped_column(String)
    basic_charge: Mapped[str] = mapped_column(String)
    tiers: Mapped[str] = mapped_column(String)
    product_id: Mapped[str] = mapped_column(String)

    product: Mapped['BtpApiManagementProducts'] = relationship('BtpApiManagementProducts', back_populates='btp_api_management_product_rate_plans')


class BtpApiManagementProxies(Base):
    __tablename__ = 'btp_api_management_proxies'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='btp_api_management_proxies_data_sources_data_source'),
        ForeignKeyConstraint(['provider_id'], ['dev.btp_api_management_providers.id'], ondelete='SET NULL', name='btp_api_management_proxies_btp_be4cfea995fe9b8792bfc64e84f027ba'),
        PrimaryKeyConstraint('id', name='btp_api_management_proxies_pkey'),
        Index('btpapimanagementproxy_name_data_source_id', 'name', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    title: Mapped[str] = mapped_column(String)
    state: Mapped[str] = mapped_column(String)
    version: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)
    created_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    created_by: Mapped[Optional[str]] = mapped_column(String)
    changed_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    changed_by: Mapped[Optional[str]] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)
    host: Mapped[Optional[str]] = mapped_column(String)
    port: Mapped[Optional[int]] = mapped_column(BigInteger)
    path: Mapped[Optional[str]] = mapped_column(String)
    provider_id: Mapped[Optional[str]] = mapped_column(String)

    btp_api_management_product: Mapped[List['BtpApiManagementProducts']] = relationship('BtpApiManagementProducts', secondary='dev.btp_api_management_proxy_products', back_populates='btp_api_management_proxy')
    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='btp_api_management_proxies')
    provider: Mapped[Optional['BtpApiManagementProviders']] = relationship('BtpApiManagementProviders', back_populates='btp_api_management_proxies')


class BtpCloudIntegrationArtefacts(Base):
    __tablename__ = 'btp_cloud_integration_artefacts'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='btp_cloud_integration_artefacts_data_sources_data_source'),
        ForeignKeyConstraint(['package_id'], ['dev.btp_cloud_integration_packages.id'], ondelete='CASCADE', name='btp_cloud_integration_artefact_faf85c39c3f5383132cb56fd4c8b3423'),
        ForeignKeyConstraint(['runtime_id'], ['dev.btp_cloud_integration_runtime_artefacts.id'], ondelete='SET NULL', name='btp_cloud_integration_artefact_decdd4da9434fd123d37a8ab687db643'),
        PrimaryKeyConstraint('id', name='btp_cloud_integration_artefacts_pkey'),
        Index('btpcloudintegrationartefact_key_type_data_source_id', 'key', 'type', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    key: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    version: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)
    package_id: Mapped[str] = mapped_column(String)
    created_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    created_by: Mapped[Optional[str]] = mapped_column(String)
    changed_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    changed_by: Mapped[Optional[str]] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)
    sender: Mapped[Optional[str]] = mapped_column(String)
    receiver: Mapped[Optional[str]] = mapped_column(String)
    runtime_id: Mapped[Optional[str]] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='btp_cloud_integration_artefacts')
    package: Mapped['BtpCloudIntegrationPackages'] = relationship('BtpCloudIntegrationPackages', back_populates='btp_cloud_integration_artefacts')
    runtime: Mapped[Optional['BtpCloudIntegrationRuntimeArtefacts']] = relationship('BtpCloudIntegrationRuntimeArtefacts', back_populates='btp_cloud_integration_artefacts')
    btp_cloud_integration_configurations: Mapped[List['BtpCloudIntegrationConfigurations']] = relationship('BtpCloudIntegrationConfigurations', back_populates='artefact')
    btp_cloud_integration_participants: Mapped[List['BtpCloudIntegrationParticipants']] = relationship('BtpCloudIntegrationParticipants', back_populates='artefact')
    btp_cloud_integration_resources: Mapped[List['BtpCloudIntegrationResources']] = relationship('BtpCloudIntegrationResources', back_populates='artefact')


class BtpCloudIntegrationMessageAttachments(Base):
    __tablename__ = 'btp_cloud_integration_message_attachments'
    __table_args__ = (
        ForeignKeyConstraint(['message_id'], ['dev.btp_cloud_integration_messages.id'], ondelete='CASCADE', name='btp_cloud_integration_message__913a96d6e73db48cee851198a5385df1'),
        PrimaryKeyConstraint('id', name='btp_cloud_integration_message_attachments_pkey'),
        Index('btpcloudintegrationmessageattachment_name_message_id', 'name', 'message_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    content_type: Mapped[str] = mapped_column(String)
    size: Mapped[int] = mapped_column(BigInteger)
    source: Mapped[bytes] = mapped_column(LargeBinary)
    message_id: Mapped[str] = mapped_column(String)

    message: Mapped['BtpCloudIntegrationMessages'] = relationship('BtpCloudIntegrationMessages', back_populates='btp_cloud_integration_message_attachments')


class BtpCloudIntegrationMessageProperties(Base):
    __tablename__ = 'btp_cloud_integration_message_properties'
    __table_args__ = (
        ForeignKeyConstraint(['message_id'], ['dev.btp_cloud_integration_messages.id'], ondelete='CASCADE', name='btp_cloud_integration_message__2eb88ca3de63851bc9df6f5748a2c7f0'),
        PrimaryKeyConstraint('id', name='btp_cloud_integration_message_properties_pkey'),
        Index('btpcloudintegrationmessageproperty_name_message_id', 'name', 'message_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    value: Mapped[str] = mapped_column(String)
    message_id: Mapped[str] = mapped_column(String)

    message: Mapped['BtpCloudIntegrationMessages'] = relationship('BtpCloudIntegrationMessages', back_populates='btp_cloud_integration_message_properties')


class BtpCloudIntegrationMessageStoreEntries(Base):
    __tablename__ = 'btp_cloud_integration_message_store_entries'
    __table_args__ = (
        ForeignKeyConstraint(['message_id'], ['dev.btp_cloud_integration_messages.id'], ondelete='CASCADE', name='btp_cloud_integration_message__b2ba4e52a37cd82202c2a23b34f009b0'),
        PrimaryKeyConstraint('id', name='btp_cloud_integration_message_store_entries_pkey'),
        Index('btpcloudintegrationmessagestoreentry_entry_message_id', 'entry', 'message_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    entry: Mapped[str] = mapped_column(String)
    created_on: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    source: Mapped[bytes] = mapped_column(LargeBinary)
    message_id: Mapped[str] = mapped_column(String)

    message: Mapped['BtpCloudIntegrationMessages'] = relationship('BtpCloudIntegrationMessages', back_populates='btp_cloud_integration_message_store_entries')


class BtpCloudIntegrationOauth2credentials(Base):
    __tablename__ = 'btp_cloud_integration_oauth2credentials'
    __table_args__ = (
        ForeignKeyConstraint(['credential_id'], ['dev.btp_cloud_integration_credentials.id'], ondelete='CASCADE', name='btp_cloud_integration_oauth2cr_ea7cf68cc17125a0a0870609db2cdd13'),
        PrimaryKeyConstraint('id', name='btp_cloud_integration_oauth2credentials_pkey'),
        Index('btp_cloud_integration_oauth2credentials_credential_id_key', 'credential_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    authentication: Mapped[str] = mapped_column(String)
    scope: Mapped[str] = mapped_column(String)
    content_type: Mapped[str] = mapped_column(String)
    token_url: Mapped[str] = mapped_column(String)
    credential_id: Mapped[str] = mapped_column(String)

    credential: Mapped['BtpCloudIntegrationCredentials'] = relationship('BtpCloudIntegrationCredentials', back_populates='btp_cloud_integration_oauth2credentials')


class BtpCloudIntegrationPackageTags(Base):
    __tablename__ = 'btp_cloud_integration_package_tags'
    __table_args__ = (
        ForeignKeyConstraint(['package_id'], ['dev.btp_cloud_integration_packages.id'], ondelete='CASCADE', name='btp_cloud_integration_package__c6374a0d2ba307896097bdb8186875e0'),
        PrimaryKeyConstraint('id', name='btp_cloud_integration_package_tags_pkey'),
        Index('btpcloudintegrationpackagetag_name_package_id', 'name', 'package_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    value: Mapped[str] = mapped_column(String)
    package_id: Mapped[str] = mapped_column(String)

    package: Mapped['BtpCloudIntegrationPackages'] = relationship('BtpCloudIntegrationPackages', back_populates='btp_cloud_integration_package_tags')


class BtpCloudIntegrationServiceEndpoints(Base):
    __tablename__ = 'btp_cloud_integration_service_endpoints'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='btp_cloud_integration_service__57593f7ade505c08cc223beff3983fd5'),
        ForeignKeyConstraint(['runtime_id'], ['dev.btp_cloud_integration_runtime_artefacts.id'], ondelete='CASCADE', name='btp_cloud_integration_service__ba34142fe797520a6243e1863bde1475'),
        PrimaryKeyConstraint('id', name='btp_cloud_integration_service_endpoints_pkey'),
        Index('btpcloudintegrationserviceendpoint_name_data_source_id', 'name', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    version: Mapped[str] = mapped_column(String)
    protocol: Mapped[str] = mapped_column(String)
    changed_on: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    url: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)
    runtime_id: Mapped[Optional[str]] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='btp_cloud_integration_service_endpoints')
    runtime: Mapped[Optional['BtpCloudIntegrationRuntimeArtefacts']] = relationship('BtpCloudIntegrationRuntimeArtefacts', back_populates='btp_cloud_integration_service_endpoints')


t_btp_event_mesh_queue_topics = Table(
    'btp_event_mesh_queue_topics', Base.metadata,
    Column('btp_event_mesh_queue_id', String, primary_key=True, nullable=False),
    Column('btp_event_mesh_topic_id', String, primary_key=True, nullable=False),
    ForeignKeyConstraint(['btp_event_mesh_queue_id'], ['dev.btp_event_mesh_queues.id'], ondelete='CASCADE', name='btp_event_mesh_queue_topics_btp_event_mesh_queue_id'),
    ForeignKeyConstraint(['btp_event_mesh_topic_id'], ['dev.btp_event_mesh_topics.id'], ondelete='CASCADE', name='btp_event_mesh_queue_topics_btp_event_mesh_topic_id'),
    PrimaryKeyConstraint('btp_event_mesh_queue_id', 'btp_event_mesh_topic_id', name='btp_event_mesh_queue_topics_pkey'),
    schema='dev'
)


class BtpEventMeshWebhooks(Base):
    __tablename__ = 'btp_event_mesh_webhooks'
    __table_args__ = (
        ForeignKeyConstraint(['btp_event_mesh_queue_web_hooks'], ['dev.btp_event_mesh_queues.id'], ondelete='SET NULL', name='btp_event_mesh_webhooks_btp_event_mesh_queues_web_hooks'),
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='btp_event_mesh_webhooks_data_sources_data_source'),
        PrimaryKeyConstraint('id', name='btp_event_mesh_webhooks_pkey'),
        Index('btpeventmeshwebhook_name_data_source_id', 'name', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    endpoint: Mapped[str] = mapped_column(String)
    on_premise: Mapped[bool] = mapped_column(Boolean)
    handshake_status: Mapped[str] = mapped_column(String)
    subscription_status: Mapped[str] = mapped_column(String)
    subscription_status_reason: Mapped[str] = mapped_column(String)
    quality_of_service: Mapped[int] = mapped_column(BigInteger)
    data_source_id: Mapped[str] = mapped_column(String)
    cloud_connector_location: Mapped[Optional[str]] = mapped_column(String)
    btp_event_mesh_queue_web_hooks: Mapped[Optional[str]] = mapped_column(String)

    btp_event_mesh_queues: Mapped[Optional['BtpEventMeshQueues']] = relationship('BtpEventMeshQueues', back_populates='btp_event_mesh_webhooks')
    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='btp_event_mesh_webhooks')


class DataFlowItems(Base):
    __tablename__ = 'data_flow_items'
    __table_args__ = (
        ForeignKeyConstraint(['data_flow_id'], ['dev.data_flows.id'], ondelete='CASCADE', name='data_flow_items_data_flows_items'),
        ForeignKeyConstraint(['inventory_id'], ['dev.inventories.id'], ondelete='CASCADE', name='data_flow_items_inventories_inventory'),
        PrimaryKeyConstraint('id', name='data_flow_items_pkey'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    sequence: Mapped[int] = mapped_column(BigInteger)
    data_flow_id: Mapped[str] = mapped_column(String)
    inventory_id: Mapped[str] = mapped_column(String)

    data_flow: Mapped['DataFlows'] = relationship('DataFlows', back_populates='data_flow_items')
    inventory: Mapped['Inventories'] = relationship('Inventories', back_populates='data_flow_items')


class Metadata(Base):
    __tablename__ = 'metadata'
    __table_args__ = (
        ForeignKeyConstraint(['inventory_id'], ['dev.inventories.id'], ondelete='CASCADE', name='metadata_inventories_metadata'),
        ForeignKeyConstraint(['system_id'], ['dev.systems.id'], ondelete='CASCADE', name='metadata_systems_metadata'),
        PrimaryKeyConstraint('id', name='metadata_pkey'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    value: Mapped[str] = mapped_column(String)
    inventory_id: Mapped[Optional[str]] = mapped_column(String)
    system_id: Mapped[Optional[str]] = mapped_column(String)

    inventory: Mapped[Optional['Inventories']] = relationship('Inventories', back_populates='metadata_')
    system: Mapped[Optional['Systems']] = relationship('Systems', back_populates='metadata_')


class ProCommunicationComponents(Base):
    __tablename__ = 'pro_communication_components'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='pro_communication_components_data_sources_data_source'),
        ForeignKeyConstraint(['pro_communication_party_components'], ['dev.pro_communication_parties.id'], ondelete='SET NULL', name='pro_communication_components_p_d4891bef34b2235fb90dd28d8c2c643b'),
        PrimaryKeyConstraint('id', name='pro_communication_components_pkey'),
        Index('procommunicationcomponent_party_name_name_data_source_id', 'party_name', 'name', 'data_source_id'),
        Index('procommunicationcomponent_party_name_name_type_data_source_id', 'party_name', 'name', 'type', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    responsible: Mapped[str] = mapped_column(String)
    changed_on: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    changed_by: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)
    folder: Mapped[Optional[str]] = mapped_column(String)
    party_name: Mapped[Optional[str]] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)
    third_party: Mapped[Optional[bool]] = mapped_column(Boolean)
    business_process: Mapped[Optional[bool]] = mapped_column(Boolean)
    pro_communication_party_components: Mapped[Optional[str]] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='pro_communication_components')
    pro_communication_parties: Mapped[Optional['ProCommunicationParties']] = relationship('ProCommunicationParties', back_populates='pro_communication_components')
    pro_configuration_scenario: Mapped[List['ProConfigurationScenarios']] = relationship('ProConfigurationScenarios', secondary='dev.pro_configuration_scenario_components', back_populates='pro_communication_component')
    pro_communication_channels: Mapped[List['ProCommunicationChannels']] = relationship('ProCommunicationChannels', back_populates='component')
    pro_agreements: Mapped[List['ProAgreements']] = relationship('ProAgreements', foreign_keys='[ProAgreements.pro_agreement_receiver_component]', back_populates='pro_communication_components')
    pro_agreements_: Mapped[List['ProAgreements']] = relationship('ProAgreements', foreign_keys='[ProAgreements.pro_agreement_sender_component]', back_populates='pro_communication_components_')
    pro_integrated_configurations: Mapped[List['ProIntegratedConfigurations']] = relationship('ProIntegratedConfigurations', back_populates='pro_communication_components')
    pro_integrated_configuration_receivers: Mapped[List['ProIntegratedConfigurationReceivers']] = relationship('ProIntegratedConfigurationReceivers', back_populates='component')


t_pro_configuration_scenario_parties = Table(
    'pro_configuration_scenario_parties', Base.metadata,
    Column('pro_configuration_scenario_id', String, primary_key=True, nullable=False),
    Column('pro_communication_party_id', String, primary_key=True, nullable=False),
    ForeignKeyConstraint(['pro_communication_party_id'], ['dev.pro_communication_parties.id'], ondelete='CASCADE', name='pro_configuration_scenario_parties_pro_communication_party_id'),
    ForeignKeyConstraint(['pro_configuration_scenario_id'], ['dev.pro_configuration_scenarios.id'], ondelete='CASCADE', name='pro_configuration_scenario_par_a26317b9b6086766aadb6acc926cbe4c'),
    PrimaryKeyConstraint('pro_configuration_scenario_id', 'pro_communication_party_id', name='pro_configuration_scenario_parties_pkey'),
    schema='dev'
)


class ProPerformanceData(Base):
    __tablename__ = 'pro_performance_data'
    __table_args__ = (
        ForeignKeyConstraint(['query_id'], ['dev.pro_performance_queries.id'], name='pro_performance_data_pro_performance_queries_data'),
        PrimaryKeyConstraint('id', name='pro_performance_data_pkey'),
        Index('properformancedata_sender_part_12f6f46969ac9f81b48a92e4b8510770', 'sender_party', 'sender_service', 'receiver_party', 'receiver_service', 'interface_name', 'query_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    inbound_channel: Mapped[str] = mapped_column(String)
    outbound_channel: Mapped[str] = mapped_column(String)
    direction: Mapped[str] = mapped_column(String)
    qos: Mapped[str] = mapped_column(String)
    server_node: Mapped[str] = mapped_column(String)
    sender_service: Mapped[str] = mapped_column(String)
    receiver_service: Mapped[str] = mapped_column(String)
    interface_name: Mapped[str] = mapped_column(String)
    namespace: Mapped[str] = mapped_column(String)
    scenario: Mapped[str] = mapped_column(String)
    is_test: Mapped[bool] = mapped_column(Boolean)
    count: Mapped[int] = mapped_column(BigInteger)
    max_size: Mapped[int] = mapped_column(BigInteger)
    min_size: Mapped[int] = mapped_column(BigInteger)
    avg_size: Mapped[int] = mapped_column(BigInteger)
    max_retries: Mapped[int] = mapped_column(BigInteger)
    min_retries: Mapped[int] = mapped_column(BigInteger)
    avg_retries: Mapped[int] = mapped_column(BigInteger)
    avg_runtime: Mapped[int] = mapped_column(BigInteger)
    total_runtime: Mapped[int] = mapped_column(BigInteger)
    query_id: Mapped[str] = mapped_column(String)
    sender_party: Mapped[Optional[str]] = mapped_column(String)
    receiver_party: Mapped[Optional[str]] = mapped_column(String)

    query: Mapped['ProPerformanceQueries'] = relationship('ProPerformanceQueries', back_populates='pro_performance_data')
    pro_performance_measure_points: Mapped[List['ProPerformanceMeasurePoints']] = relationship('ProPerformanceMeasurePoints', back_populates='data')


class Properties(Base):
    __tablename__ = 'properties'
    __table_args__ = (
        ForeignKeyConstraint(['data_flow_id'], ['dev.data_flows.id'], ondelete='CASCADE', name='properties_data_flows_properties'),
        ForeignKeyConstraint(['inventory_id'], ['dev.inventories.id'], ondelete='CASCADE', name='properties_inventories_properties'),
        ForeignKeyConstraint(['system_id'], ['dev.systems.id'], ondelete='CASCADE', name='properties_systems_properties'),
        ForeignKeyConstraint(['type_id'], ['dev.property_types.id'], ondelete='CASCADE', name='properties_property_types_type'),
        PrimaryKeyConstraint('id', name='properties_pkey'),
        Index('property_type_id_data_flow_id_inventory_id_system_id', 'type_id', 'data_flow_id', 'inventory_id', 'system_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    type_id: Mapped[str] = mapped_column(String)
    value: Mapped[Optional[str]] = mapped_column(String)
    data_flow_id: Mapped[Optional[str]] = mapped_column(String)
    inventory_id: Mapped[Optional[str]] = mapped_column(String)
    system_id: Mapped[Optional[str]] = mapped_column(String)

    data_flow: Mapped[Optional['DataFlows']] = relationship('DataFlows', back_populates='properties')
    inventory: Mapped[Optional['Inventories']] = relationship('Inventories', back_populates='properties')
    system: Mapped[Optional['Systems']] = relationship('Systems', back_populates='properties')
    type: Mapped['PropertyTypes'] = relationship('PropertyTypes', back_populates='properties')


class TaskRuns(Base):
    __tablename__ = 'task_runs'
    __table_args__ = (
        ForeignKeyConstraint(['task_id'], ['dev.tasks.id'], name='task_runs_tasks_runs'),
        PrimaryKeyConstraint('id', name='task_runs_pkey'),
        Index('taskrun_start_time_task_id', 'start_time', 'task_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    start_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    task_id: Mapped[str] = mapped_column(String)
    end_time: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    duration: Mapped[Optional[int]] = mapped_column(BigInteger)
    successful: Mapped[Optional[bool]] = mapped_column(Boolean)

    task: Mapped['Tasks'] = relationship('Tasks', back_populates='task_runs')


class AbapOutboundPartnerProfiles(Base):
    __tablename__ = 'abap_outbound_partner_profiles'
    __table_args__ = (
        ForeignKeyConstraint(['abap_outbound_partner_profile_receiver_port'], ['dev.abap_ports.id'], name='abap_outbound_partner_profiles_abap_ports_receiver_port'),
        ForeignKeyConstraint(['profile_id'], ['dev.abap_partner_profiles.id'], ondelete='CASCADE', name='abap_outbound_partner_profiles_abap_partner_profiles_outbound'),
        PrimaryKeyConstraint('id', name='abap_outbound_partner_profiles_pkey'),
        Index('abap_outbound_partner_profiles_profile_id_key', 'profile_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    output_mode: Mapped[str] = mapped_column(String)
    basic_type: Mapped[str] = mapped_column(String)
    extension: Mapped[str] = mapped_column(String)
    package_size: Mapped[str] = mapped_column(String)
    abap_outbound_partner_profile_receiver_port: Mapped[str] = mapped_column(String)
    profile_id: Mapped[str] = mapped_column(String)

    abap_ports: Mapped['AbapPorts'] = relationship('AbapPorts', back_populates='abap_outbound_partner_profiles')
    profile: Mapped['AbapPartnerProfiles'] = relationship('AbapPartnerProfiles', back_populates='abap_outbound_partner_profiles')


class AbapSoapServiceBindingProperties(Base):
    __tablename__ = 'abap_soap_service_binding_properties'
    __table_args__ = (
        ForeignKeyConstraint(['binding_id'], ['dev.abap_soap_service_bindings.id'], name='abap_soap_service_binding_prop_d37a99a9bd075eaaaac85380d8063872'),
        PrimaryKeyConstraint('id', name='abap_soap_service_binding_properties_pkey'),
        Index('abapsoapservicebindingproperty_type_subject_name_binding_id', 'type', 'subject', 'name', 'binding_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    type: Mapped[str] = mapped_column(String)
    subject: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    value: Mapped[str] = mapped_column(String)
    binding_id: Mapped[str] = mapped_column(String)

    binding: Mapped['AbapSoapServiceBindings'] = relationship('AbapSoapServiceBindings', back_populates='abap_soap_service_binding_properties')


class AzureResourceGroups(Base):
    __tablename__ = 'azure_resource_groups'
    __table_args__ = (
        ForeignKeyConstraint(['subscription_id'], ['dev.azure_subscriptions.id'], name='azure_resource_groups_azure_subscriptions_resource_groups'),
        PrimaryKeyConstraint('id', name='azure_resource_groups_pkey'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    subscription_id: Mapped[str] = mapped_column(String)
    category: Mapped[Optional[str]] = mapped_column(String)

    subscription: Mapped['AzureSubscriptions'] = relationship('AzureSubscriptions', back_populates='azure_resource_groups')
    azure_api_management_services: Mapped[List['AzureApiManagementServices']] = relationship('AzureApiManagementServices', back_populates='resource_group')
    azure_event_grid_domains: Mapped[List['AzureEventGridDomains']] = relationship('AzureEventGridDomains', back_populates='resource_group')
    azure_event_grid_partner_namespaces: Mapped[List['AzureEventGridPartnerNamespaces']] = relationship('AzureEventGridPartnerNamespaces', back_populates='resource_group')
    azure_event_grid_partner_registrations: Mapped[List['AzureEventGridPartnerRegistrations']] = relationship('AzureEventGridPartnerRegistrations', back_populates='resource_group')
    azure_event_grid_partner_topics: Mapped[List['AzureEventGridPartnerTopics']] = relationship('AzureEventGridPartnerTopics', back_populates='resource_group')
    azure_event_grid_system_topics: Mapped[List['AzureEventGridSystemTopics']] = relationship('AzureEventGridSystemTopics', back_populates='resource_group')
    azure_event_grid_topics: Mapped[List['AzureEventGridTopics']] = relationship('AzureEventGridTopics', back_populates='resource_group')
    azure_logic_app_integration_accounts: Mapped[List['AzureLogicAppIntegrationAccounts']] = relationship('AzureLogicAppIntegrationAccounts', back_populates='resource_group')
    azure_logic_app_workflows: Mapped[List['AzureLogicAppWorkflows']] = relationship('AzureLogicAppWorkflows', back_populates='resource_group')
    azure_service_bus_namespaces: Mapped[List['AzureServiceBusNamespaces']] = relationship('AzureServiceBusNamespaces', back_populates='resource_group')
    azure_standard_apps: Mapped[List['AzureStandardApps']] = relationship('AzureStandardApps', back_populates='resource_group')
    azure_api_management_apis: Mapped[List['AzureApiManagementApis']] = relationship('AzureApiManagementApis', back_populates='resource_group')
    azure_api_management_backends: Mapped[List['AzureApiManagementBackends']] = relationship('AzureApiManagementBackends', back_populates='resource_group')
    azure_api_management_products: Mapped[List['AzureApiManagementProducts']] = relationship('AzureApiManagementProducts', back_populates='resource_group')
    azure_service_bus_queues: Mapped[List['AzureServiceBusQueues']] = relationship('AzureServiceBusQueues', back_populates='resource_group')
    azure_service_bus_topics: Mapped[List['AzureServiceBusTopics']] = relationship('AzureServiceBusTopics', back_populates='resource_group')
    azure_api_management_policies: Mapped[List['AzureApiManagementPolicies']] = relationship('AzureApiManagementPolicies', back_populates='resource_group')
    azure_api_management_subscriptions: Mapped[List['AzureApiManagementSubscriptions']] = relationship('AzureApiManagementSubscriptions', back_populates='resource_group')
    azure_event_grid_event_subscriptions: Mapped[List['AzureEventGridEventSubscriptions']] = relationship('AzureEventGridEventSubscriptions', back_populates='resource_group')


t_btp_api_management_proxy_products = Table(
    'btp_api_management_proxy_products', Base.metadata,
    Column('btp_api_management_proxy_id', String, primary_key=True, nullable=False),
    Column('btp_api_management_product_id', String, primary_key=True, nullable=False),
    ForeignKeyConstraint(['btp_api_management_product_id'], ['dev.btp_api_management_products.id'], ondelete='CASCADE', name='btp_api_management_proxy_products_btp_api_management_product_id'),
    ForeignKeyConstraint(['btp_api_management_proxy_id'], ['dev.btp_api_management_proxies.id'], ondelete='CASCADE', name='btp_api_management_proxy_products_btp_api_management_proxy_id'),
    PrimaryKeyConstraint('btp_api_management_proxy_id', 'btp_api_management_product_id', name='btp_api_management_proxy_products_pkey'),
    schema='dev'
)


class BtpCloudIntegrationConfigurations(Base):
    __tablename__ = 'btp_cloud_integration_configurations'
    __table_args__ = (
        ForeignKeyConstraint(['artefact_id'], ['dev.btp_cloud_integration_artefacts.id'], ondelete='CASCADE', name='btp_cloud_integration_configur_1cbc774da4c1acfb7936c39d4542ddac'),
        PrimaryKeyConstraint('id', name='btp_cloud_integration_configurations_pkey'),
        Index('btpcloudintegrationconfiguration_name_artefact_id', 'name', 'artefact_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    value: Mapped[str] = mapped_column(String)
    artefact_id: Mapped[str] = mapped_column(String)

    artefact: Mapped['BtpCloudIntegrationArtefacts'] = relationship('BtpCloudIntegrationArtefacts', back_populates='btp_cloud_integration_configurations')


class BtpCloudIntegrationParticipants(Base):
    __tablename__ = 'btp_cloud_integration_participants'
    __table_args__ = (
        ForeignKeyConstraint(['artefact_id'], ['dev.btp_cloud_integration_artefacts.id'], ondelete='CASCADE', name='btp_cloud_integration_particip_861239df5e55a11f34582f1830502a4d'),
        PrimaryKeyConstraint('id', name='btp_cloud_integration_participants_pkey'),
        Index('btpcloudintegrationparticipant_key_artefact_id', 'key', 'artefact_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    key: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    artefact_id: Mapped[str] = mapped_column(String)

    artefact: Mapped['BtpCloudIntegrationArtefacts'] = relationship('BtpCloudIntegrationArtefacts', back_populates='btp_cloud_integration_participants')
    btp_cloud_integration_connections: Mapped[List['BtpCloudIntegrationConnections']] = relationship('BtpCloudIntegrationConnections', back_populates='participant')


class BtpCloudIntegrationResources(Base):
    __tablename__ = 'btp_cloud_integration_resources'
    __table_args__ = (
        ForeignKeyConstraint(['artefact_id'], ['dev.btp_cloud_integration_artefacts.id'], ondelete='CASCADE', name='btp_cloud_integration_resource_c6c5ee9fe113b7abb357b75d2da503df'),
        PrimaryKeyConstraint('id', name='btp_cloud_integration_resources_pkey'),
        Index('btpcloudintegrationresource_key_type_artefact_id', 'key', 'type', 'artefact_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    checksum: Mapped[int] = mapped_column(BigInteger)
    source: Mapped[bytes] = mapped_column(LargeBinary)
    artefact_id: Mapped[str] = mapped_column(String)
    key: Mapped[str] = mapped_column(String)
    created_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    created_by: Mapped[Optional[str]] = mapped_column(String)
    changed_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    changed_by: Mapped[Optional[str]] = mapped_column(String)

    artefact: Mapped['BtpCloudIntegrationArtefacts'] = relationship('BtpCloudIntegrationArtefacts', back_populates='btp_cloud_integration_resources')


class ProCommunicationChannels(Base):
    __tablename__ = 'pro_communication_channels'
    __table_args__ = (
        ForeignKeyConstraint(['component_id'], ['dev.pro_communication_components.id'], ondelete='CASCADE', name='pro_communication_channels_pro_5bd3440bf113511528be9289e9860a11'),
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='pro_communication_channels_data_sources_data_source'),
        ForeignKeyConstraint(['party_id'], ['dev.pro_communication_parties.id'], ondelete='SET NULL', name='pro_communication_channels_pro_communication_parties_channels'),
        PrimaryKeyConstraint('id', name='pro_communication_channels_pkey'),
        Index('procommunicationchannel_party__bc4a00028060913ffeca6ed2080c5f60', 'party_name', 'component_name', 'name', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    responsible: Mapped[str] = mapped_column(String)
    changed_on: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    changed_by: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    namespace: Mapped[str] = mapped_column(String)
    software_component: Mapped[str] = mapped_column(String)
    direction: Mapped[str] = mapped_column(String)
    transport_protocol: Mapped[str] = mapped_column(String)
    message_protocol: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)
    folder: Mapped[Optional[str]] = mapped_column(String)
    party_name: Mapped[Optional[str]] = mapped_column(String)
    component_name: Mapped[Optional[str]] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)
    transport_protocol_version: Mapped[Optional[str]] = mapped_column(String)
    message_protocol_version: Mapped[Optional[str]] = mapped_column(String)
    adapter_engine: Mapped[Optional[str]] = mapped_column(String)
    component_id: Mapped[Optional[str]] = mapped_column(String)
    party_id: Mapped[Optional[str]] = mapped_column(String)

    component: Mapped[Optional['ProCommunicationComponents']] = relationship('ProCommunicationComponents', back_populates='pro_communication_channels')
    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='pro_communication_channels')
    party: Mapped[Optional['ProCommunicationParties']] = relationship('ProCommunicationParties', back_populates='pro_communication_channels')
    pro_configuration_scenario: Mapped[List['ProConfigurationScenarios']] = relationship('ProConfigurationScenarios', secondary='dev.pro_configuration_scenario_channels', back_populates='pro_communication_channel')
    pro_adapter_attributes: Mapped[List['ProAdapterAttributes']] = relationship('ProAdapterAttributes', back_populates='channel')
    pro_adapter_modules: Mapped[List['ProAdapterModules']] = relationship('ProAdapterModules', back_populates='channel')
    pro_agreements: Mapped[List['ProAgreements']] = relationship('ProAgreements', back_populates='pro_communication_channels')
    pro_integrated_configurations: Mapped[List['ProIntegratedConfigurations']] = relationship('ProIntegratedConfigurations', back_populates='pro_communication_channels')
    pro_integrated_configuration_interfaces: Mapped[List['ProIntegratedConfigurationInterfaces']] = relationship('ProIntegratedConfigurationInterfaces', back_populates='pro_communication_channels')


t_pro_configuration_scenario_components = Table(
    'pro_configuration_scenario_components', Base.metadata,
    Column('pro_configuration_scenario_id', String, primary_key=True, nullable=False),
    Column('pro_communication_component_id', String, primary_key=True, nullable=False),
    ForeignKeyConstraint(['pro_communication_component_id'], ['dev.pro_communication_components.id'], ondelete='CASCADE', name='pro_configuration_scenario_com_c2b8facd7dc720459df2b467d0338f77'),
    ForeignKeyConstraint(['pro_configuration_scenario_id'], ['dev.pro_configuration_scenarios.id'], ondelete='CASCADE', name='pro_configuration_scenario_com_7bbd713fa8a56cf2b28e53cb47c366f8'),
    PrimaryKeyConstraint('pro_configuration_scenario_id', 'pro_communication_component_id', name='pro_configuration_scenario_components_pkey'),
    schema='dev'
)


class ProPerformanceMeasurePoints(Base):
    __tablename__ = 'pro_performance_measure_points'
    __table_args__ = (
        ForeignKeyConstraint(['data_id'], ['dev.pro_performance_data.id'], name='pro_performance_measure_points_5b20363c8ddc4631eb4281ad39fedf75'),
        PrimaryKeyConstraint('id', name='pro_performance_measure_points_pkey'),
        Index('properformancemeasurepoint_name_data_id', 'name', 'data_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    sequence: Mapped[int] = mapped_column(SmallInteger)
    name: Mapped[str] = mapped_column(String)
    min: Mapped[int] = mapped_column(BigInteger)
    max: Mapped[int] = mapped_column(BigInteger)
    avg: Mapped[int] = mapped_column(BigInteger)
    data_id: Mapped[str] = mapped_column(String)

    data: Mapped['ProPerformanceData'] = relationship('ProPerformanceData', back_populates='pro_performance_measure_points')


class AzureApiManagementServices(Base):
    __tablename__ = 'azure_api_management_services'
    __table_args__ = (
        ForeignKeyConstraint(['resource_group_id'], ['dev.azure_resource_groups.id'], ondelete='CASCADE', name='azure_api_management_services__16ad9c5948895ee3240b056be5583574'),
        PrimaryKeyConstraint('id', name='azure_api_management_services_pkey'),
        Index('azureapimanagementservice_name_resource_group_id', 'name', 'resource_group_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    gateway_url: Mapped[str] = mapped_column(String)
    developer_portal_url: Mapped[str] = mapped_column(String)
    resource_group_id: Mapped[str] = mapped_column(String)
    tags: Mapped[Optional[bytes]] = mapped_column(LargeBinary)

    resource_group: Mapped['AzureResourceGroups'] = relationship('AzureResourceGroups', back_populates='azure_api_management_services')
    azure_api_management_apis: Mapped[List['AzureApiManagementApis']] = relationship('AzureApiManagementApis', back_populates='service')
    azure_api_management_backends: Mapped[List['AzureApiManagementBackends']] = relationship('AzureApiManagementBackends', back_populates='service')
    azure_api_management_products: Mapped[List['AzureApiManagementProducts']] = relationship('AzureApiManagementProducts', back_populates='service')
    azure_api_management_policies: Mapped[List['AzureApiManagementPolicies']] = relationship('AzureApiManagementPolicies', back_populates='service')
    azure_api_management_subscriptions: Mapped[List['AzureApiManagementSubscriptions']] = relationship('AzureApiManagementSubscriptions', back_populates='service')


class AzureEventGridDomains(Base):
    __tablename__ = 'azure_event_grid_domains'
    __table_args__ = (
        ForeignKeyConstraint(['resource_group_id'], ['dev.azure_resource_groups.id'], ondelete='CASCADE', name='azure_event_grid_domains_azure_9e0a50137ccba3b68d339d01934cbf33'),
        PrimaryKeyConstraint('id', name='azure_event_grid_domains_pkey'),
        Index('azureeventgriddomain_name_resource_group_id', 'name', 'resource_group_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    endpoint: Mapped[str] = mapped_column(String)
    input_schema: Mapped[str] = mapped_column(String)
    sku: Mapped[str] = mapped_column(String)
    resource_group_id: Mapped[str] = mapped_column(String)
    tags: Mapped[Optional[bytes]] = mapped_column(LargeBinary)

    resource_group: Mapped['AzureResourceGroups'] = relationship('AzureResourceGroups', back_populates='azure_event_grid_domains')
    azure_event_grid_domain_topics: Mapped[List['AzureEventGridDomainTopics']] = relationship('AzureEventGridDomainTopics', back_populates='domain')
    azure_event_grid_event_subscriptions: Mapped[List['AzureEventGridEventSubscriptions']] = relationship('AzureEventGridEventSubscriptions', back_populates='azure_event_grid_domains')


class AzureEventGridPartnerNamespaces(Base):
    __tablename__ = 'azure_event_grid_partner_namespaces'
    __table_args__ = (
        ForeignKeyConstraint(['resource_group_id'], ['dev.azure_resource_groups.id'], ondelete='CASCADE', name='azure_event_grid_partner_names_8041809f83e4e4789cc653ff3877423c'),
        PrimaryKeyConstraint('id', name='azure_event_grid_partner_namespaces_pkey'),
        Index('azureeventgridpartnernamespace_name_resource_group_id', 'name', 'resource_group_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    endpoint: Mapped[str] = mapped_column(String)
    resource_group_id: Mapped[str] = mapped_column(String)
    tags: Mapped[Optional[bytes]] = mapped_column(LargeBinary)

    resource_group: Mapped['AzureResourceGroups'] = relationship('AzureResourceGroups', back_populates='azure_event_grid_partner_namespaces')
    azure_event_grid_partner_namespace_channels: Mapped[List['AzureEventGridPartnerNamespaceChannels']] = relationship('AzureEventGridPartnerNamespaceChannels', back_populates='namespace')


class AzureEventGridPartnerRegistrations(Base):
    __tablename__ = 'azure_event_grid_partner_registrations'
    __table_args__ = (
        ForeignKeyConstraint(['resource_group_id'], ['dev.azure_resource_groups.id'], ondelete='CASCADE', name='azure_event_grid_partner_regis_4b75e0863f474ad69459ae9b433f0288'),
        PrimaryKeyConstraint('id', name='azure_event_grid_partner_registrations_pkey'),
        Index('azureeventgridpartnerregistration_name_resource_group_id', 'name', 'resource_group_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    identifier: Mapped[str] = mapped_column(String)
    resource_group_id: Mapped[str] = mapped_column(String)
    tags: Mapped[Optional[bytes]] = mapped_column(LargeBinary)

    resource_group: Mapped['AzureResourceGroups'] = relationship('AzureResourceGroups', back_populates='azure_event_grid_partner_registrations')


class AzureEventGridPartnerTopics(Base):
    __tablename__ = 'azure_event_grid_partner_topics'
    __table_args__ = (
        ForeignKeyConstraint(['resource_group_id'], ['dev.azure_resource_groups.id'], ondelete='CASCADE', name='azure_event_grid_partner_topic_165b9c4d0ab8a915a99329d69b48163d'),
        PrimaryKeyConstraint('id', name='azure_event_grid_partner_topics_pkey'),
        Index('azureeventgridpartnertopic_name_resource_group_id', 'name', 'resource_group_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    source: Mapped[str] = mapped_column(String)
    activation_state: Mapped[str] = mapped_column(String)
    resource_group_id: Mapped[str] = mapped_column(String)
    tags: Mapped[Optional[bytes]] = mapped_column(LargeBinary)

    resource_group: Mapped['AzureResourceGroups'] = relationship('AzureResourceGroups', back_populates='azure_event_grid_partner_topics')
    azure_event_grid_event_subscriptions: Mapped[List['AzureEventGridEventSubscriptions']] = relationship('AzureEventGridEventSubscriptions', back_populates='azure_event_grid_partner_topics')


class AzureEventGridSystemTopics(Base):
    __tablename__ = 'azure_event_grid_system_topics'
    __table_args__ = (
        ForeignKeyConstraint(['resource_group_id'], ['dev.azure_resource_groups.id'], ondelete='CASCADE', name='azure_event_grid_system_topics_3897e2a42238a632822c156ad35d93b7'),
        PrimaryKeyConstraint('id', name='azure_event_grid_system_topics_pkey'),
        Index('azureeventgridsystemtopic_name_resource_group_id', 'name', 'resource_group_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    source: Mapped[str] = mapped_column(String)
    resource_group_id: Mapped[str] = mapped_column(String)
    tags: Mapped[Optional[bytes]] = mapped_column(LargeBinary)

    resource_group: Mapped['AzureResourceGroups'] = relationship('AzureResourceGroups', back_populates='azure_event_grid_system_topics')
    azure_event_grid_event_subscriptions: Mapped[List['AzureEventGridEventSubscriptions']] = relationship('AzureEventGridEventSubscriptions', back_populates='azure_event_grid_system_topics')


class AzureEventGridTopics(Base):
    __tablename__ = 'azure_event_grid_topics'
    __table_args__ = (
        ForeignKeyConstraint(['resource_group_id'], ['dev.azure_resource_groups.id'], ondelete='CASCADE', name='azure_event_grid_topics_azure_resource_groups_event_grid_topics'),
        PrimaryKeyConstraint('id', name='azure_event_grid_topics_pkey'),
        Index('azureeventgridtopic_name_resource_group_id', 'name', 'resource_group_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    endpoint: Mapped[str] = mapped_column(String)
    input_schema: Mapped[str] = mapped_column(String)
    sku: Mapped[str] = mapped_column(String)
    resource_group_id: Mapped[str] = mapped_column(String)
    tags: Mapped[Optional[bytes]] = mapped_column(LargeBinary)

    resource_group: Mapped['AzureResourceGroups'] = relationship('AzureResourceGroups', back_populates='azure_event_grid_topics')
    azure_event_grid_event_subscriptions: Mapped[List['AzureEventGridEventSubscriptions']] = relationship('AzureEventGridEventSubscriptions', back_populates='azure_event_grid_topics')


class AzureLogicAppIntegrationAccounts(Base):
    __tablename__ = 'azure_logic_app_integration_accounts'
    __table_args__ = (
        ForeignKeyConstraint(['resource_group_id'], ['dev.azure_resource_groups.id'], ondelete='CASCADE', name='azure_logic_app_integration_ac_9f7023144a4c89410b3fee9fedb4c552'),
        PrimaryKeyConstraint('id', name='azure_logic_app_integration_accounts_pkey'),
        Index('azurelogicappintegrationaccount_name_resource_group_id', 'name', 'resource_group_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    state: Mapped[str] = mapped_column(String)
    sku: Mapped[str] = mapped_column(String)
    resource_group_id: Mapped[str] = mapped_column(String)
    tags: Mapped[Optional[bytes]] = mapped_column(LargeBinary)

    resource_group: Mapped['AzureResourceGroups'] = relationship('AzureResourceGroups', back_populates='azure_logic_app_integration_accounts')
    azure_logic_app_integration_account_certificates: Mapped[List['AzureLogicAppIntegrationAccountCertificates']] = relationship('AzureLogicAppIntegrationAccountCertificates', back_populates='account')
    azure_logic_app_integration_account_maps: Mapped[List['AzureLogicAppIntegrationAccountMaps']] = relationship('AzureLogicAppIntegrationAccountMaps', back_populates='account')
    azure_logic_app_integration_account_partners: Mapped[List['AzureLogicAppIntegrationAccountPartners']] = relationship('AzureLogicAppIntegrationAccountPartners', back_populates='account')
    azure_logic_app_integration_account_schemas: Mapped[List['AzureLogicAppIntegrationAccountSchemas']] = relationship('AzureLogicAppIntegrationAccountSchemas', back_populates='account')
    azure_logic_app_integration_account_sessions: Mapped[List['AzureLogicAppIntegrationAccountSessions']] = relationship('AzureLogicAppIntegrationAccountSessions', back_populates='account')
    azure_logic_app_integration_account_agreements: Mapped[List['AzureLogicAppIntegrationAccountAgreements']] = relationship('AzureLogicAppIntegrationAccountAgreements', back_populates='account')


class AzureLogicAppWorkflows(Base):
    __tablename__ = 'azure_logic_app_workflows'
    __table_args__ = (
        ForeignKeyConstraint(['resource_group_id'], ['dev.azure_resource_groups.id'], ondelete='CASCADE', name='azure_logic_app_workflows_azur_65aee42f1fa2e77097b64aba7ceafd7c'),
        PrimaryKeyConstraint('id', name='azure_logic_app_workflows_pkey'),
        Index('azurelogicappworkflow_name_resource_group_id', 'name', 'resource_group_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    state: Mapped[str] = mapped_column(String)
    version: Mapped[str] = mapped_column(String)
    access_endpoint: Mapped[str] = mapped_column(String)
    definition: Mapped[bytes] = mapped_column(LargeBinary)
    parameters: Mapped[bytes] = mapped_column(LargeBinary)
    resource_group_id: Mapped[str] = mapped_column(String)
    created_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    created_by: Mapped[Optional[str]] = mapped_column(String)
    changed_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    changed_by: Mapped[Optional[str]] = mapped_column(String)
    tags: Mapped[Optional[bytes]] = mapped_column(LargeBinary)

    resource_group: Mapped['AzureResourceGroups'] = relationship('AzureResourceGroups', back_populates='azure_logic_app_workflows')
    azure_logic_app_workflow_versions: Mapped[List['AzureLogicAppWorkflowVersions']] = relationship('AzureLogicAppWorkflowVersions', back_populates='workflow')


class AzureServiceBusNamespaces(Base):
    __tablename__ = 'azure_service_bus_namespaces'
    __table_args__ = (
        ForeignKeyConstraint(['resource_group_id'], ['dev.azure_resource_groups.id'], ondelete='CASCADE', name='azure_service_bus_namespaces_a_e388b6b27d8286b2c53fae5713427587'),
        PrimaryKeyConstraint('id', name='azure_service_bus_namespaces_pkey'),
        Index('azureservicebusnamespace_name_resource_group_id', 'name', 'resource_group_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    endpoint: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    resource_group_id: Mapped[str] = mapped_column(String)
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    tags: Mapped[Optional[bytes]] = mapped_column(LargeBinary)

    resource_group: Mapped['AzureResourceGroups'] = relationship('AzureResourceGroups', back_populates='azure_service_bus_namespaces')
    azure_service_bus_queues: Mapped[List['AzureServiceBusQueues']] = relationship('AzureServiceBusQueues', back_populates='namespace')
    azure_service_bus_topics: Mapped[List['AzureServiceBusTopics']] = relationship('AzureServiceBusTopics', back_populates='namespace')
    azure_service_bus_authorization_rules: Mapped[List['AzureServiceBusAuthorizationRules']] = relationship('AzureServiceBusAuthorizationRules', back_populates='namespace')


class AzureStandardApps(Base):
    __tablename__ = 'azure_standard_apps'
    __table_args__ = (
        ForeignKeyConstraint(['resource_group_id'], ['dev.azure_resource_groups.id'], ondelete='CASCADE', name='azure_standard_apps_azure_resource_groups_standard_apps'),
        PrimaryKeyConstraint('id', name='azure_standard_apps_pkey'),
        Index('azurestandardapp_name_resource_group_id', 'name', 'resource_group_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    kind: Mapped[str] = mapped_column(String)
    resource_group_id: Mapped[str] = mapped_column(String)
    tags: Mapped[Optional[bytes]] = mapped_column(LargeBinary)

    resource_group: Mapped['AzureResourceGroups'] = relationship('AzureResourceGroups', back_populates='azure_standard_apps')
    azure_standard_app_workflows: Mapped[List['AzureStandardAppWorkflows']] = relationship('AzureStandardAppWorkflows', back_populates='app')


class BtpCloudIntegrationConnections(Base):
    __tablename__ = 'btp_cloud_integration_connections'
    __table_args__ = (
        ForeignKeyConstraint(['credential_id'], ['dev.btp_cloud_integration_credentials.id'], ondelete='SET NULL', name='btp_cloud_integration_connecti_4b793dcb476b87a42aae6d2a150279af'),
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='btp_cloud_integration_connections_data_sources_data_source'),
        ForeignKeyConstraint(['participant_id'], ['dev.btp_cloud_integration_participants.id'], ondelete='CASCADE', name='btp_cloud_integration_connecti_72832586bcfeb894029103fac99108cf'),
        PrimaryKeyConstraint('id', name='btp_cloud_integration_connections_pkey'),
        Index('btpcloudintegrationconnection_key_participant_id', 'key', 'participant_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)
    participant_id: Mapped[str] = mapped_column(String)
    key: Mapped[str] = mapped_column(String)
    version: Mapped[Optional[str]] = mapped_column(String)
    address: Mapped[Optional[str]] = mapped_column(String)
    credential_name: Mapped[Optional[str]] = mapped_column(String)
    credential_id: Mapped[Optional[str]] = mapped_column(String)

    credential: Mapped[Optional['BtpCloudIntegrationCredentials']] = relationship('BtpCloudIntegrationCredentials', back_populates='btp_cloud_integration_connections')
    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='btp_cloud_integration_connections')
    participant: Mapped['BtpCloudIntegrationParticipants'] = relationship('BtpCloudIntegrationParticipants', back_populates='btp_cloud_integration_connections')


class ProAdapterAttributes(Base):
    __tablename__ = 'pro_adapter_attributes'
    __table_args__ = (
        ForeignKeyConstraint(['channel_id'], ['dev.pro_communication_channels.id'], ondelete='CASCADE', name='pro_adapter_attributes_pro_communication_channels_attributes'),
        PrimaryKeyConstraint('id', name='pro_adapter_attributes_pkey'),
        Index('proadapterattribute_name_channel_id', 'name', 'channel_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    channel_id: Mapped[str] = mapped_column(String)
    value: Mapped[Optional[str]] = mapped_column(String)

    channel: Mapped['ProCommunicationChannels'] = relationship('ProCommunicationChannels', back_populates='pro_adapter_attributes')


class ProAdapterModules(Base):
    __tablename__ = 'pro_adapter_modules'
    __table_args__ = (
        ForeignKeyConstraint(['channel_id'], ['dev.pro_communication_channels.id'], ondelete='CASCADE', name='pro_adapter_modules_pro_communication_channels_modules'),
        PrimaryKeyConstraint('id', name='pro_adapter_modules_pkey'),
        Index('proadaptermodule_name_type_group_channel_id', 'name', 'type', 'group', 'channel_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    group: Mapped[str] = mapped_column(String)
    channel_id: Mapped[str] = mapped_column(String)

    channel: Mapped['ProCommunicationChannels'] = relationship('ProCommunicationChannels', back_populates='pro_adapter_modules')
    pro_adapter_module_parameters: Mapped[List['ProAdapterModuleParameters']] = relationship('ProAdapterModuleParameters', back_populates='module')


class ProAgreements(Base):
    __tablename__ = 'pro_agreements'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='pro_agreements_data_sources_data_source'),
        ForeignKeyConstraint(['pro_agreement_channel'], ['dev.pro_communication_channels.id'], ondelete='SET NULL', name='pro_agreements_pro_communication_channels_channel'),
        ForeignKeyConstraint(['pro_agreement_receiver_component'], ['dev.pro_communication_components.id'], ondelete='SET NULL', name='pro_agreements_pro_communication_components_receiver_component'),
        ForeignKeyConstraint(['pro_agreement_sender_component'], ['dev.pro_communication_components.id'], ondelete='SET NULL', name='pro_agreements_pro_communication_components_sender_component'),
        PrimaryKeyConstraint('id', name='pro_agreements_pkey'),
        Index('configuration_scenarios', 'type', 'sender_party', 'sender_name', 'interface', 'namespace', 'receiver_party', 'receiver_name', 'data_source_id', unique=True),
        Index('receiver_agreements', 'type', 'sender_party', 'sender_name', 'interface', 'namespace', 'data_source_id'),
        Index('sender_agreements', 'type', 'sender_party', 'receiver_party', 'receiver_name', 'interface', 'namespace', 'data_source_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    responsible: Mapped[str] = mapped_column(String)
    changed_on: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    changed_by: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    sender_name: Mapped[str] = mapped_column(String)
    interface: Mapped[str] = mapped_column(String)
    namespace: Mapped[str] = mapped_column(String)
    receiver_name: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)
    folder: Mapped[Optional[str]] = mapped_column(String)
    sender_party: Mapped[Optional[str]] = mapped_column(String)
    receiver_party: Mapped[Optional[str]] = mapped_column(String)
    pro_agreement_channel: Mapped[Optional[str]] = mapped_column(String)
    pro_agreement_sender_component: Mapped[Optional[str]] = mapped_column(String)
    pro_agreement_receiver_component: Mapped[Optional[str]] = mapped_column(String)

    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='pro_agreements')
    pro_communication_channels: Mapped[Optional['ProCommunicationChannels']] = relationship('ProCommunicationChannels', back_populates='pro_agreements')
    pro_communication_components: Mapped[Optional['ProCommunicationComponents']] = relationship('ProCommunicationComponents', foreign_keys=[pro_agreement_receiver_component], back_populates='pro_agreements')
    pro_communication_components_: Mapped[Optional['ProCommunicationComponents']] = relationship('ProCommunicationComponents', foreign_keys=[pro_agreement_sender_component], back_populates='pro_agreements_')
    pro_configuration_scenario: Mapped[List['ProConfigurationScenarios']] = relationship('ProConfigurationScenarios', secondary='dev.pro_configuration_scenario_receiver_agreements', back_populates='pro_agreement')
    pro_configuration_scenario_: Mapped[List['ProConfigurationScenarios']] = relationship('ProConfigurationScenarios', secondary='dev.pro_configuration_scenario_sender_agreements', back_populates='pro_agreement_')
    pro_integrated_configuration: Mapped[List['ProIntegratedConfigurations']] = relationship('ProIntegratedConfigurations', secondary='dev.pro_integrated_configuration_receiver_agreements', back_populates='pro_agreement')
    pro_integrated_configuration_: Mapped[List['ProIntegratedConfigurations']] = relationship('ProIntegratedConfigurations', secondary='dev.pro_integrated_configuration_sender_agreements', back_populates='pro_agreement_')


t_pro_configuration_scenario_channels = Table(
    'pro_configuration_scenario_channels', Base.metadata,
    Column('pro_configuration_scenario_id', String, primary_key=True, nullable=False),
    Column('pro_communication_channel_id', String, primary_key=True, nullable=False),
    ForeignKeyConstraint(['pro_communication_channel_id'], ['dev.pro_communication_channels.id'], ondelete='CASCADE', name='pro_configuration_scenario_cha_411c4da3c7aa472ed9c1f177193a32a7'),
    ForeignKeyConstraint(['pro_configuration_scenario_id'], ['dev.pro_configuration_scenarios.id'], ondelete='CASCADE', name='pro_configuration_scenario_cha_ac89a1870e2ccb6a00a77e4a92b9c0d1'),
    PrimaryKeyConstraint('pro_configuration_scenario_id', 'pro_communication_channel_id', name='pro_configuration_scenario_channels_pkey'),
    schema='dev'
)


class ProIntegratedConfigurations(Base):
    __tablename__ = 'pro_integrated_configurations'
    __table_args__ = (
        ForeignKeyConstraint(['data_source_id'], ['dev.data_sources.id'], name='pro_integrated_configurations_data_sources_data_source'),
        ForeignKeyConstraint(['pro_integrated_configuration_sender_channel'], ['dev.pro_communication_channels.id'], ondelete='SET NULL', name='pro_integrated_configurations__f8133d7e05d2f7406bebe247b2f043e8'),
        ForeignKeyConstraint(['pro_integrated_configuration_sender_component'], ['dev.pro_communication_components.id'], ondelete='SET NULL', name='pro_integrated_configurations__09aadd714ff395576253007d74119f70'),
        PrimaryKeyConstraint('id', name='pro_integrated_configurations_pkey'),
        Index('prointegratedconfiguration_name_namespace_data_source_id', 'name', 'namespace', 'data_source_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    responsible: Mapped[str] = mapped_column(String)
    changed_on: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    changed_by: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    interface: Mapped[str] = mapped_column(String)
    namespace: Mapped[str] = mapped_column(String)
    data_source_id: Mapped[str] = mapped_column(String)
    folder: Mapped[Optional[str]] = mapped_column(String)
    virtual_receiver: Mapped[Optional[str]] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)
    logging: Mapped[Optional[str]] = mapped_column(String)
    staging: Mapped[Optional[str]] = mapped_column(String)
    pro_integrated_configuration_sender_component: Mapped[Optional[str]] = mapped_column(String)
    pro_integrated_configuration_sender_channel: Mapped[Optional[str]] = mapped_column(String)

    pro_configuration_scenario: Mapped[List['ProConfigurationScenarios']] = relationship('ProConfigurationScenarios', secondary='dev.pro_configuration_scenario_configurations', back_populates='pro_integrated_configuration')
    pro_agreement: Mapped[List['ProAgreements']] = relationship('ProAgreements', secondary='dev.pro_integrated_configuration_receiver_agreements', back_populates='pro_integrated_configuration')
    pro_agreement_: Mapped[List['ProAgreements']] = relationship('ProAgreements', secondary='dev.pro_integrated_configuration_sender_agreements', back_populates='pro_integrated_configuration_')
    data_source: Mapped['DataSources'] = relationship('DataSources', back_populates='pro_integrated_configurations')
    pro_communication_channels: Mapped[Optional['ProCommunicationChannels']] = relationship('ProCommunicationChannels', back_populates='pro_integrated_configurations')
    pro_communication_components: Mapped[Optional['ProCommunicationComponents']] = relationship('ProCommunicationComponents', back_populates='pro_integrated_configurations')
    pro_integrated_configuration_receivers: Mapped[List['ProIntegratedConfigurationReceivers']] = relationship('ProIntegratedConfigurationReceivers', back_populates='configuration')


class AzureApiManagementApis(Base):
    __tablename__ = 'azure_api_management_apis'
    __table_args__ = (
        ForeignKeyConstraint(['resource_group_id'], ['dev.azure_resource_groups.id'], ondelete='CASCADE', name='azure_api_management_apis_azur_2fae6646e7e8ebf7bcea713049f58131'),
        ForeignKeyConstraint(['service_id'], ['dev.azure_api_management_services.id'], name='azure_api_management_apis_azure_api_management_services_apis'),
        PrimaryKeyConstraint('id', name='azure_api_management_apis_pkey'),
        Index('azureapimanagementapi_name_service_id', 'name', 'service_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    display_name: Mapped[str] = mapped_column(String)
    revision: Mapped[str] = mapped_column(String)
    is_current: Mapped[bool] = mapped_column(Boolean)
    service_url: Mapped[str] = mapped_column(String)
    service_id: Mapped[str] = mapped_column(String)
    resource_group_id: Mapped[str] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)

    resource_group: Mapped['AzureResourceGroups'] = relationship('AzureResourceGroups', back_populates='azure_api_management_apis')
    service: Mapped['AzureApiManagementServices'] = relationship('AzureApiManagementServices', back_populates='azure_api_management_apis')
    azure_api_management_product: Mapped[List['AzureApiManagementProducts']] = relationship('AzureApiManagementProducts', secondary='dev.azure_api_management_api_products', back_populates='azure_api_management_api')
    azure_api_management_api_operations: Mapped[List['AzureApiManagementApiOperations']] = relationship('AzureApiManagementApiOperations', back_populates='api')
    azure_api_management_api_revisions: Mapped[List['AzureApiManagementApiRevisions']] = relationship('AzureApiManagementApiRevisions', back_populates='api')
    azure_api_management_policies: Mapped[List['AzureApiManagementPolicies']] = relationship('AzureApiManagementPolicies', back_populates='api')


class AzureApiManagementBackends(Base):
    __tablename__ = 'azure_api_management_backends'
    __table_args__ = (
        ForeignKeyConstraint(['resource_group_id'], ['dev.azure_resource_groups.id'], ondelete='CASCADE', name='azure_api_management_backends__33edc53b30de2e80624b479f96465fa3'),
        ForeignKeyConstraint(['service_id'], ['dev.azure_api_management_services.id'], name='azure_api_management_backends__35eebb848a6e9fe8c6417244bd5760b9'),
        PrimaryKeyConstraint('id', name='azure_api_management_backends_pkey'),
        Index('azureapimanagementbackend_name_service_id', 'name', 'service_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    url: Mapped[str] = mapped_column(String)
    protocol: Mapped[str] = mapped_column(String)
    service_id: Mapped[str] = mapped_column(String)
    resource_group_id: Mapped[str] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)
    authorization_scheme: Mapped[Optional[str]] = mapped_column(String)
    authorization_parameter: Mapped[Optional[str]] = mapped_column(String)

    resource_group: Mapped['AzureResourceGroups'] = relationship('AzureResourceGroups', back_populates='azure_api_management_backends')
    service: Mapped['AzureApiManagementServices'] = relationship('AzureApiManagementServices', back_populates='azure_api_management_backends')
    azure_api_management_backend_parameters: Mapped[List['AzureApiManagementBackendParameters']] = relationship('AzureApiManagementBackendParameters', back_populates='backend')


class AzureApiManagementProducts(Base):
    __tablename__ = 'azure_api_management_products'
    __table_args__ = (
        ForeignKeyConstraint(['resource_group_id'], ['dev.azure_resource_groups.id'], ondelete='CASCADE', name='azure_api_management_products__2722d5c3fcefe7d669d4ac72a4564abc'),
        ForeignKeyConstraint(['service_id'], ['dev.azure_api_management_services.id'], ondelete='SET NULL', name='azure_api_management_products__fae3e71f4c5bfabf475bafd2bb55e228'),
        PrimaryKeyConstraint('id', name='azure_api_management_products_pkey'),
        Index('azureapimanagementproduct_name_service_id', 'name', 'service_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    display_name: Mapped[str] = mapped_column(String)
    approval_required: Mapped[bool] = mapped_column(Boolean)
    subscription_required: Mapped[bool] = mapped_column(Boolean)
    subscriptions_limit: Mapped[int] = mapped_column(BigInteger)
    state: Mapped[str] = mapped_column(String)
    resource_group_id: Mapped[str] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)
    terms: Mapped[Optional[str]] = mapped_column(String)
    service_id: Mapped[Optional[str]] = mapped_column(String)

    azure_api_management_api: Mapped[List['AzureApiManagementApis']] = relationship('AzureApiManagementApis', secondary='dev.azure_api_management_api_products', back_populates='azure_api_management_product')
    resource_group: Mapped['AzureResourceGroups'] = relationship('AzureResourceGroups', back_populates='azure_api_management_products')
    service: Mapped[Optional['AzureApiManagementServices']] = relationship('AzureApiManagementServices', back_populates='azure_api_management_products')
    azure_api_management_policies: Mapped[List['AzureApiManagementPolicies']] = relationship('AzureApiManagementPolicies', back_populates='product')
    azure_api_management_subscriptions: Mapped[List['AzureApiManagementSubscriptions']] = relationship('AzureApiManagementSubscriptions', back_populates='product')


class AzureEventGridDomainTopics(Base):
    __tablename__ = 'azure_event_grid_domain_topics'
    __table_args__ = (
        ForeignKeyConstraint(['domain_id'], ['dev.azure_event_grid_domains.id'], name='azure_event_grid_domain_topics_azure_event_grid_domains_topics'),
        PrimaryKeyConstraint('id', name='azure_event_grid_domain_topics_pkey'),
        Index('azureeventgriddomaintopic_name_domain_id', 'name', 'domain_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    domain_id: Mapped[str] = mapped_column(String)

    domain: Mapped['AzureEventGridDomains'] = relationship('AzureEventGridDomains', back_populates='azure_event_grid_domain_topics')
    azure_event_grid_event_subscriptions: Mapped[List['AzureEventGridEventSubscriptions']] = relationship('AzureEventGridEventSubscriptions', back_populates='azure_event_grid_domain_topics')


class AzureEventGridPartnerNamespaceChannels(Base):
    __tablename__ = 'azure_event_grid_partner_namespace_channels'
    __table_args__ = (
        ForeignKeyConstraint(['namespace_id'], ['dev.azure_event_grid_partner_namespaces.id'], name='azure_event_grid_partner_names_3546b81457dbd817d48d0ea98cf8cbf5'),
        PrimaryKeyConstraint('id', name='azure_event_grid_partner_namespace_channels_pkey'),
        Index('azureeventgridpartnernamespacechannel_name_namespace_id', 'name', 'namespace_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    partner_topic_name: Mapped[str] = mapped_column(String)
    partner_topic_source: Mapped[str] = mapped_column(String)
    readiness_state: Mapped[str] = mapped_column(String)
    namespace_id: Mapped[str] = mapped_column(String)

    namespace: Mapped['AzureEventGridPartnerNamespaces'] = relationship('AzureEventGridPartnerNamespaces', back_populates='azure_event_grid_partner_namespace_channels')


class AzureLogicAppIntegrationAccountCertificates(Base):
    __tablename__ = 'azure_logic_app_integration_account_certificates'
    __table_args__ = (
        ForeignKeyConstraint(['account_id'], ['dev.azure_logic_app_integration_accounts.id'], name='azure_logic_app_integration_ac_a52d0941015716bf73cb972cec5a7647'),
        PrimaryKeyConstraint('id', name='azure_logic_app_integration_account_certificates_pkey'),
        Index('azurelogicappintegrationaccountcertificate_name_account_id', 'name', 'account_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    account_id: Mapped[str] = mapped_column(String)
    key_vault: Mapped[Optional[str]] = mapped_column(String)
    key_name: Mapped[Optional[str]] = mapped_column(String)
    certificate: Mapped[Optional[str]] = mapped_column(String)

    account: Mapped['AzureLogicAppIntegrationAccounts'] = relationship('AzureLogicAppIntegrationAccounts', back_populates='azure_logic_app_integration_account_certificates')


class AzureLogicAppIntegrationAccountMaps(Base):
    __tablename__ = 'azure_logic_app_integration_account_maps'
    __table_args__ = (
        ForeignKeyConstraint(['account_id'], ['dev.azure_logic_app_integration_accounts.id'], name='azure_logic_app_integration_ac_4d202ed08a6af934397e7f8abab70a9d'),
        PrimaryKeyConstraint('id', name='azure_logic_app_integration_account_maps_pkey'),
        Index('azurelogicappintegrationaccountmap_name_type_account_id', 'name', 'type', 'account_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    size: Mapped[int] = mapped_column(BigInteger)
    source: Mapped[bytes] = mapped_column(LargeBinary)
    account_id: Mapped[str] = mapped_column(String)

    account: Mapped['AzureLogicAppIntegrationAccounts'] = relationship('AzureLogicAppIntegrationAccounts', back_populates='azure_logic_app_integration_account_maps')


class AzureLogicAppIntegrationAccountPartners(Base):
    __tablename__ = 'azure_logic_app_integration_account_partners'
    __table_args__ = (
        ForeignKeyConstraint(['account_id'], ['dev.azure_logic_app_integration_accounts.id'], name='azure_logic_app_integration_ac_3863aef1dbf76da3f763333102f01775'),
        PrimaryKeyConstraint('id', name='azure_logic_app_integration_account_partners_pkey'),
        Index('azurelogicappintegrationaccountpartner_name_type_account_id', 'name', 'type', 'account_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    account_id: Mapped[str] = mapped_column(String)
    classification: Mapped[Optional[str]] = mapped_column(String)
    contact_name: Mapped[Optional[str]] = mapped_column(String)
    contact_email: Mapped[Optional[str]] = mapped_column(String)
    contact_phone: Mapped[Optional[str]] = mapped_column(String)
    contact_fax: Mapped[Optional[str]] = mapped_column(String)
    supply_chain_code: Mapped[Optional[str]] = mapped_column(String)

    account: Mapped['AzureLogicAppIntegrationAccounts'] = relationship('AzureLogicAppIntegrationAccounts', back_populates='azure_logic_app_integration_account_partners')
    azure_logic_app_integration_account_agreements: Mapped[List['AzureLogicAppIntegrationAccountAgreements']] = relationship('AzureLogicAppIntegrationAccountAgreements', foreign_keys='[AzureLogicAppIntegrationAccountAgreements.guest_partner_id]', back_populates='guest_partner')
    azure_logic_app_integration_account_agreements_: Mapped[List['AzureLogicAppIntegrationAccountAgreements']] = relationship('AzureLogicAppIntegrationAccountAgreements', foreign_keys='[AzureLogicAppIntegrationAccountAgreements.host_partner_id]', back_populates='host_partner')
    azure_logic_app_integration_account_partner_identities: Mapped[List['AzureLogicAppIntegrationAccountPartnerIdentities']] = relationship('AzureLogicAppIntegrationAccountPartnerIdentities', back_populates='partner')
    azure_logic_app_integration_account_partner_metadata: Mapped[List['AzureLogicAppIntegrationAccountPartnerMetadata']] = relationship('AzureLogicAppIntegrationAccountPartnerMetadata', back_populates='partner')


class AzureLogicAppIntegrationAccountSchemas(Base):
    __tablename__ = 'azure_logic_app_integration_account_schemas'
    __table_args__ = (
        ForeignKeyConstraint(['account_id'], ['dev.azure_logic_app_integration_accounts.id'], name='azure_logic_app_integration_ac_36e35592f6a5405d8117597c31cc9646'),
        PrimaryKeyConstraint('id', name='azure_logic_app_integration_account_schemas_pkey'),
        Index('azurelogicappintegrationaccountschema_name_type_account_id', 'name', 'type', 'account_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    document: Mapped[str] = mapped_column(String)
    namespace: Mapped[str] = mapped_column(String)
    size: Mapped[int] = mapped_column(BigInteger)
    source: Mapped[bytes] = mapped_column(LargeBinary)
    account_id: Mapped[str] = mapped_column(String)

    account: Mapped['AzureLogicAppIntegrationAccounts'] = relationship('AzureLogicAppIntegrationAccounts', back_populates='azure_logic_app_integration_account_schemas')


class AzureLogicAppIntegrationAccountSessions(Base):
    __tablename__ = 'azure_logic_app_integration_account_sessions'
    __table_args__ = (
        ForeignKeyConstraint(['account_id'], ['dev.azure_logic_app_integration_accounts.id'], name='azure_logic_app_integration_ac_490e9ddad1504bcf4bf7968daf5da681'),
        PrimaryKeyConstraint('id', name='azure_logic_app_integration_account_sessions_pkey'),
        Index('azurelogicappintegrationaccountsession_name_account_id', 'name', 'account_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    properties: Mapped[bytes] = mapped_column(LargeBinary)
    account_id: Mapped[str] = mapped_column(String)

    account: Mapped['AzureLogicAppIntegrationAccounts'] = relationship('AzureLogicAppIntegrationAccounts', back_populates='azure_logic_app_integration_account_sessions')


class AzureLogicAppWorkflowVersions(Base):
    __tablename__ = 'azure_logic_app_workflow_versions'
    __table_args__ = (
        ForeignKeyConstraint(['workflow_id'], ['dev.azure_logic_app_workflows.id'], name='azure_logic_app_workflow_versi_b3003ef9ee2b525589216d1cd0ee9d06'),
        PrimaryKeyConstraint('id', name='azure_logic_app_workflow_versions_pkey'),
        Index('azurelogicappworkflowversion_name_version_workflow_id', 'name', 'version', 'workflow_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    version: Mapped[str] = mapped_column(String)
    definition: Mapped[bytes] = mapped_column(LargeBinary)
    parameters: Mapped[bytes] = mapped_column(LargeBinary)
    workflow_id: Mapped[str] = mapped_column(String)
    created_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    created_by: Mapped[Optional[str]] = mapped_column(String)
    changed_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    changed_by: Mapped[Optional[str]] = mapped_column(String)

    workflow: Mapped['AzureLogicAppWorkflows'] = relationship('AzureLogicAppWorkflows', back_populates='azure_logic_app_workflow_versions')


class AzureServiceBusQueues(Base):
    __tablename__ = 'azure_service_bus_queues'
    __table_args__ = (
        ForeignKeyConstraint(['namespace_id'], ['dev.azure_service_bus_namespaces.id'], name='azure_service_bus_queues_azure_service_bus_namespaces_queues'),
        ForeignKeyConstraint(['resource_group_id'], ['dev.azure_resource_groups.id'], ondelete='CASCADE', name='azure_service_bus_queues_azure_fa7a7b8f93fac12980d3683261ee0942'),
        PrimaryKeyConstraint('id', name='azure_service_bus_queues_pkey'),
        Index('azureservicebusqueue_name_namespace_id', 'name', 'namespace_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    url: Mapped[str] = mapped_column(String)
    lock_duration: Mapped[str] = mapped_column(String)
    default_time_to_live: Mapped[str] = mapped_column(String)
    delete_on_idle: Mapped[str] = mapped_column(String)
    size_in_bytes: Mapped[int] = mapped_column(BigInteger)
    max_size_in_megabytes: Mapped[int] = mapped_column(BigInteger)
    free_space: Mapped[int] = mapped_column(BigInteger)
    max_delivery_count: Mapped[int] = mapped_column(BigInteger)
    message_count: Mapped[int] = mapped_column(BigInteger)
    message_active_count: Mapped[int] = mapped_column(BigInteger)
    message_scheduled_count: Mapped[int] = mapped_column(BigInteger)
    message_transfer_count: Mapped[int] = mapped_column(BigInteger)
    dead_letter_expired: Mapped[bool] = mapped_column(Boolean)
    dead_letter_count: Mapped[int] = mapped_column(BigInteger)
    dead_letter_transfer_count: Mapped[int] = mapped_column(BigInteger)
    duplicate_detection: Mapped[bool] = mapped_column(Boolean)
    partitioning: Mapped[bool] = mapped_column(Boolean)
    session_handling: Mapped[bool] = mapped_column(Boolean)
    status: Mapped[str] = mapped_column(String)
    resource_group_id: Mapped[str] = mapped_column(String)
    namespace_id: Mapped[str] = mapped_column(String)
    created_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    created_by: Mapped[Optional[str]] = mapped_column(String)
    changed_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    changed_by: Mapped[Optional[str]] = mapped_column(String)
    message_forward_to: Mapped[Optional[str]] = mapped_column(String)
    dead_letter_forward_to: Mapped[Optional[str]] = mapped_column(String)
    accessed_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))

    namespace: Mapped['AzureServiceBusNamespaces'] = relationship('AzureServiceBusNamespaces', back_populates='azure_service_bus_queues')
    resource_group: Mapped['AzureResourceGroups'] = relationship('AzureResourceGroups', back_populates='azure_service_bus_queues')
    azure_service_bus_authorization_rules: Mapped[List['AzureServiceBusAuthorizationRules']] = relationship('AzureServiceBusAuthorizationRules', back_populates='queue')


class AzureServiceBusTopics(Base):
    __tablename__ = 'azure_service_bus_topics'
    __table_args__ = (
        ForeignKeyConstraint(['namespace_id'], ['dev.azure_service_bus_namespaces.id'], name='azure_service_bus_topics_azure_service_bus_namespaces_topics'),
        ForeignKeyConstraint(['resource_group_id'], ['dev.azure_resource_groups.id'], ondelete='CASCADE', name='azure_service_bus_topics_azure_021431e520eb8aff8af503e59d7fc793'),
        PrimaryKeyConstraint('id', name='azure_service_bus_topics_pkey'),
        Index('azureservicebustopic_name_namespace_id', 'name', 'namespace_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    url: Mapped[str] = mapped_column(String)
    default_time_to_live: Mapped[str] = mapped_column(String)
    delete_on_idle: Mapped[str] = mapped_column(String)
    size_in_bytes: Mapped[int] = mapped_column(BigInteger)
    max_size_in_megabytes: Mapped[int] = mapped_column(BigInteger)
    free_space: Mapped[int] = mapped_column(BigInteger)
    subscription_count: Mapped[int] = mapped_column(BigInteger)
    message_active_count: Mapped[int] = mapped_column(BigInteger)
    message_scheduled_count: Mapped[int] = mapped_column(BigInteger)
    message_transfer_count: Mapped[int] = mapped_column(BigInteger)
    dead_letter_count: Mapped[int] = mapped_column(BigInteger)
    dead_letter_transfer_count: Mapped[int] = mapped_column(BigInteger)
    duplicate_detection: Mapped[bool] = mapped_column(Boolean)
    partitioning: Mapped[bool] = mapped_column(Boolean)
    session_handling: Mapped[bool] = mapped_column(Boolean)
    status: Mapped[str] = mapped_column(String)
    resource_group_id: Mapped[str] = mapped_column(String)
    namespace_id: Mapped[str] = mapped_column(String)
    created_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    created_by: Mapped[Optional[str]] = mapped_column(String)
    changed_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    changed_by: Mapped[Optional[str]] = mapped_column(String)
    accessed_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))

    namespace: Mapped['AzureServiceBusNamespaces'] = relationship('AzureServiceBusNamespaces', back_populates='azure_service_bus_topics')
    resource_group: Mapped['AzureResourceGroups'] = relationship('AzureResourceGroups', back_populates='azure_service_bus_topics')
    azure_service_bus_authorization_rules: Mapped[List['AzureServiceBusAuthorizationRules']] = relationship('AzureServiceBusAuthorizationRules', back_populates='topic')
    azure_service_bus_topic_subscriptions: Mapped[List['AzureServiceBusTopicSubscriptions']] = relationship('AzureServiceBusTopicSubscriptions', back_populates='topic')


class AzureStandardAppWorkflows(Base):
    __tablename__ = 'azure_standard_app_workflows'
    __table_args__ = (
        ForeignKeyConstraint(['app_id'], ['dev.azure_standard_apps.id'], name='azure_standard_app_workflows_azure_standard_apps_workflows'),
        PrimaryKeyConstraint('id', name='azure_standard_app_workflows_pkey'),
        Index('azurestandardappworkflow_name_app_id', 'name', 'app_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    kind: Mapped[str] = mapped_column(String)
    flow_state: Mapped[str] = mapped_column(String)
    health: Mapped[str] = mapped_column(String)
    definition: Mapped[bytes] = mapped_column(LargeBinary)
    app_id: Mapped[str] = mapped_column(String)

    app: Mapped['AzureStandardApps'] = relationship('AzureStandardApps', back_populates='azure_standard_app_workflows')


class ProAdapterModuleParameters(Base):
    __tablename__ = 'pro_adapter_module_parameters'
    __table_args__ = (
        ForeignKeyConstraint(['module_id'], ['dev.pro_adapter_modules.id'], ondelete='CASCADE', name='pro_adapter_module_parameters_pro_adapter_modules_parameters'),
        PrimaryKeyConstraint('id', name='pro_adapter_module_parameters_pkey'),
        Index('proadaptermoduleparameter_name_module_id', 'name', 'module_id', unique=True),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    value: Mapped[str] = mapped_column(String)
    module_id: Mapped[str] = mapped_column(String)

    module: Mapped['ProAdapterModules'] = relationship('ProAdapterModules', back_populates='pro_adapter_module_parameters')


t_pro_configuration_scenario_configurations = Table(
    'pro_configuration_scenario_configurations', Base.metadata,
    Column('pro_configuration_scenario_id', String, primary_key=True, nullable=False),
    Column('pro_integrated_configuration_id', String, primary_key=True, nullable=False),
    ForeignKeyConstraint(['pro_configuration_scenario_id'], ['dev.pro_configuration_scenarios.id'], ondelete='CASCADE', name='pro_configuration_scenario_con_2f9eb62b58f0832f022186634f603c0e'),
    ForeignKeyConstraint(['pro_integrated_configuration_id'], ['dev.pro_integrated_configurations.id'], ondelete='CASCADE', name='pro_configuration_scenario_con_9ea09e1f241181ab5eef644c025e656d'),
    PrimaryKeyConstraint('pro_configuration_scenario_id', 'pro_integrated_configuration_id', name='pro_configuration_scenario_configurations_pkey'),
    schema='dev'
)


t_pro_configuration_scenario_receiver_agreements = Table(
    'pro_configuration_scenario_receiver_agreements', Base.metadata,
    Column('pro_configuration_scenario_id', String, primary_key=True, nullable=False),
    Column('pro_agreement_id', String, primary_key=True, nullable=False),
    ForeignKeyConstraint(['pro_agreement_id'], ['dev.pro_agreements.id'], ondelete='CASCADE', name='pro_configuration_scenario_receiver_agreements_pro_agreement_id'),
    ForeignKeyConstraint(['pro_configuration_scenario_id'], ['dev.pro_configuration_scenarios.id'], ondelete='CASCADE', name='pro_configuration_scenario_rec_3c68b11beb61b334989c46a9741f2903'),
    PrimaryKeyConstraint('pro_configuration_scenario_id', 'pro_agreement_id', name='pro_configuration_scenario_receiver_agreements_pkey'),
    schema='dev'
)


t_pro_configuration_scenario_sender_agreements = Table(
    'pro_configuration_scenario_sender_agreements', Base.metadata,
    Column('pro_configuration_scenario_id', String, primary_key=True, nullable=False),
    Column('pro_agreement_id', String, primary_key=True, nullable=False),
    ForeignKeyConstraint(['pro_agreement_id'], ['dev.pro_agreements.id'], ondelete='CASCADE', name='pro_configuration_scenario_sender_agreements_pro_agreement_id'),
    ForeignKeyConstraint(['pro_configuration_scenario_id'], ['dev.pro_configuration_scenarios.id'], ondelete='CASCADE', name='pro_configuration_scenario_sen_b1006c30d08575e44a057bffceed07bf'),
    PrimaryKeyConstraint('pro_configuration_scenario_id', 'pro_agreement_id', name='pro_configuration_scenario_sender_agreements_pkey'),
    schema='dev'
)


t_pro_integrated_configuration_receiver_agreements = Table(
    'pro_integrated_configuration_receiver_agreements', Base.metadata,
    Column('pro_integrated_configuration_id', String, primary_key=True, nullable=False),
    Column('pro_agreement_id', String, primary_key=True, nullable=False),
    ForeignKeyConstraint(['pro_agreement_id'], ['dev.pro_agreements.id'], ondelete='CASCADE', name='pro_integrated_configuration_r_5c697c840e4d1f1df38b8e547dbc8569'),
    ForeignKeyConstraint(['pro_integrated_configuration_id'], ['dev.pro_integrated_configurations.id'], ondelete='CASCADE', name='pro_integrated_configuration_r_cea702a7d6f1d1f091976ecd1d3cd322'),
    PrimaryKeyConstraint('pro_integrated_configuration_id', 'pro_agreement_id', name='pro_integrated_configuration_receiver_agreements_pkey'),
    schema='dev'
)


class ProIntegratedConfigurationReceivers(Base):
    __tablename__ = 'pro_integrated_configuration_receivers'
    __table_args__ = (
        ForeignKeyConstraint(['component_id'], ['dev.pro_communication_components.id'], ondelete='CASCADE', name='pro_integrated_configuration_r_24cf32e9566f49e831f56a87408b4018'),
        ForeignKeyConstraint(['configuration_id'], ['dev.pro_integrated_configurations.id'], ondelete='CASCADE', name='pro_integrated_configuration_r_1ec19c289c997cfc93dacb25cfbed66f'),
        PrimaryKeyConstraint('id', name='pro_integrated_configuration_receivers_pkey'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    configuration_id: Mapped[str] = mapped_column(String)
    component_id: Mapped[str] = mapped_column(String)

    component: Mapped['ProCommunicationComponents'] = relationship('ProCommunicationComponents', back_populates='pro_integrated_configuration_receivers')
    configuration: Mapped['ProIntegratedConfigurations'] = relationship('ProIntegratedConfigurations', back_populates='pro_integrated_configuration_receivers')
    pro_integrated_configuration_interfaces: Mapped[List['ProIntegratedConfigurationInterfaces']] = relationship('ProIntegratedConfigurationInterfaces', back_populates='receiver')
    pro_integrated_configuration_rules: Mapped[List['ProIntegratedConfigurationRules']] = relationship('ProIntegratedConfigurationRules', back_populates='pro_integrated_configuration_receivers')


t_pro_integrated_configuration_sender_agreements = Table(
    'pro_integrated_configuration_sender_agreements', Base.metadata,
    Column('pro_integrated_configuration_id', String, primary_key=True, nullable=False),
    Column('pro_agreement_id', String, primary_key=True, nullable=False),
    ForeignKeyConstraint(['pro_agreement_id'], ['dev.pro_agreements.id'], ondelete='CASCADE', name='pro_integrated_configuration_sender_agreements_pro_agreement_id'),
    ForeignKeyConstraint(['pro_integrated_configuration_id'], ['dev.pro_integrated_configurations.id'], ondelete='CASCADE', name='pro_integrated_configuration_s_8cef4aaeb1d38274d6c8326b81bca117'),
    PrimaryKeyConstraint('pro_integrated_configuration_id', 'pro_agreement_id', name='pro_integrated_configuration_sender_agreements_pkey'),
    schema='dev'
)


class AzureApiManagementApiOperations(Base):
    __tablename__ = 'azure_api_management_api_operations'
    __table_args__ = (
        ForeignKeyConstraint(['api_id'], ['dev.azure_api_management_apis.id'], name='azure_api_management_api_opera_7b0480db34c2ff4baba3f5b64ba9d07a'),
        PrimaryKeyConstraint('id', name='azure_api_management_api_operations_pkey'),
        Index('azureapimanagementapioperation_name_api_id', 'name', 'api_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    display_name: Mapped[str] = mapped_column(String)
    method: Mapped[str] = mapped_column(String)
    url_template: Mapped[str] = mapped_column(String)
    api_id: Mapped[str] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)

    api: Mapped['AzureApiManagementApis'] = relationship('AzureApiManagementApis', back_populates='azure_api_management_api_operations')
    azure_api_management_api_operation_replies: Mapped[List['AzureApiManagementApiOperationReplies']] = relationship('AzureApiManagementApiOperationReplies', back_populates='operation')
    azure_api_management_api_operation_parameters: Mapped[List['AzureApiManagementApiOperationParameters']] = relationship('AzureApiManagementApiOperationParameters', back_populates='operation')


t_azure_api_management_api_products = Table(
    'azure_api_management_api_products', Base.metadata,
    Column('azure_api_management_api_id', String, primary_key=True, nullable=False),
    Column('azure_api_management_product_id', String, primary_key=True, nullable=False),
    ForeignKeyConstraint(['azure_api_management_api_id'], ['dev.azure_api_management_apis.id'], ondelete='CASCADE', name='azure_api_management_api_products_azure_api_management_api_id'),
    ForeignKeyConstraint(['azure_api_management_product_id'], ['dev.azure_api_management_products.id'], ondelete='CASCADE', name='azure_api_management_api_produ_c9126aac153da16c9e3231db7fe3c163'),
    PrimaryKeyConstraint('azure_api_management_api_id', 'azure_api_management_product_id', name='azure_api_management_api_products_pkey'),
    schema='dev'
)


class AzureApiManagementApiRevisions(Base):
    __tablename__ = 'azure_api_management_api_revisions'
    __table_args__ = (
        ForeignKeyConstraint(['api_id'], ['dev.azure_api_management_apis.id'], name='azure_api_management_api_revis_779e82e23d15f2af126d45a2473af89d'),
        PrimaryKeyConstraint('id', name='azure_api_management_api_revisions_pkey'),
        Index('azureapimanagementapirevision_name_api_id', 'name', 'api_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    is_current: Mapped[bool] = mapped_column(Boolean)
    is_online: Mapped[bool] = mapped_column(Boolean)
    api_id: Mapped[str] = mapped_column(String)
    created_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    created_by: Mapped[Optional[str]] = mapped_column(String)
    changed_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    changed_by: Mapped[Optional[str]] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)

    api: Mapped['AzureApiManagementApis'] = relationship('AzureApiManagementApis', back_populates='azure_api_management_api_revisions')


class AzureApiManagementBackendParameters(Base):
    __tablename__ = 'azure_api_management_backend_parameters'
    __table_args__ = (
        ForeignKeyConstraint(['backend_id'], ['dev.azure_api_management_backends.id'], name='azure_api_management_backend_p_d888f5a170551d06a84b14ef38d2e78b'),
        PrimaryKeyConstraint('id', name='azure_api_management_backend_parameters_pkey'),
        Index('azureapimanagementbackendparameter_name_type_backend_id', 'name', 'type', 'backend_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    value: Mapped[str] = mapped_column(String)
    backend_id: Mapped[str] = mapped_column(String)

    backend: Mapped['AzureApiManagementBackends'] = relationship('AzureApiManagementBackends', back_populates='azure_api_management_backend_parameters')


class AzureApiManagementPolicies(Base):
    __tablename__ = 'azure_api_management_policies'
    __table_args__ = (
        ForeignKeyConstraint(['api_id'], ['dev.azure_api_management_apis.id'], ondelete='SET NULL', name='azure_api_management_policies__a1ea728f5a3a66a1838bbb563c2703de'),
        ForeignKeyConstraint(['product_id'], ['dev.azure_api_management_products.id'], ondelete='SET NULL', name='azure_api_management_policies__754cdd144fd8f355f843fa366d13b2aa'),
        ForeignKeyConstraint(['resource_group_id'], ['dev.azure_resource_groups.id'], ondelete='CASCADE', name='azure_api_management_policies__31863da374455252f346060d87270e1d'),
        ForeignKeyConstraint(['service_id'], ['dev.azure_api_management_services.id'], ondelete='SET NULL', name='azure_api_management_policies__0db5c14866cde71873f846507cf05fd1'),
        PrimaryKeyConstraint('id', name='azure_api_management_policies_pkey'),
        Index('azureapimanagementpolicy_name_resource_group_id', 'name', 'resource_group_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    resource_group_id: Mapped[str] = mapped_column(String)
    api_id: Mapped[Optional[str]] = mapped_column(String)
    product_id: Mapped[Optional[str]] = mapped_column(String)
    service_id: Mapped[Optional[str]] = mapped_column(String)

    api: Mapped[Optional['AzureApiManagementApis']] = relationship('AzureApiManagementApis', back_populates='azure_api_management_policies')
    product: Mapped[Optional['AzureApiManagementProducts']] = relationship('AzureApiManagementProducts', back_populates='azure_api_management_policies')
    resource_group: Mapped['AzureResourceGroups'] = relationship('AzureResourceGroups', back_populates='azure_api_management_policies')
    service: Mapped[Optional['AzureApiManagementServices']] = relationship('AzureApiManagementServices', back_populates='azure_api_management_policies')
    azure_api_management_policy_properties: Mapped[List['AzureApiManagementPolicyProperties']] = relationship('AzureApiManagementPolicyProperties', back_populates='policy')


class AzureApiManagementSubscriptions(Base):
    __tablename__ = 'azure_api_management_subscriptions'
    __table_args__ = (
        ForeignKeyConstraint(['product_id'], ['dev.azure_api_management_products.id'], ondelete='SET NULL', name='azure_api_management_subscript_c345ff745aecd008a935cc3782dc8315'),
        ForeignKeyConstraint(['resource_group_id'], ['dev.azure_resource_groups.id'], ondelete='CASCADE', name='azure_api_management_subscript_231b6fecc7fe9b37c8791198f7a61e96'),
        ForeignKeyConstraint(['service_id'], ['dev.azure_api_management_services.id'], ondelete='SET NULL', name='azure_api_management_subscript_926b87ee3d575e9b2413b06a60d272fc'),
        PrimaryKeyConstraint('id', name='azure_api_management_subscriptions_pkey'),
        Index('azureapimanagementsubscription_name_resource_group_id', 'name', 'resource_group_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    display_name: Mapped[str] = mapped_column(String)
    state: Mapped[str] = mapped_column(String)
    scope: Mapped[str] = mapped_column(String)
    created_on: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    resource_group_id: Mapped[str] = mapped_column(String)
    started_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    ended_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    product_id: Mapped[Optional[str]] = mapped_column(String)
    service_id: Mapped[Optional[str]] = mapped_column(String)

    product: Mapped[Optional['AzureApiManagementProducts']] = relationship('AzureApiManagementProducts', back_populates='azure_api_management_subscriptions')
    resource_group: Mapped['AzureResourceGroups'] = relationship('AzureResourceGroups', back_populates='azure_api_management_subscriptions')
    service: Mapped[Optional['AzureApiManagementServices']] = relationship('AzureApiManagementServices', back_populates='azure_api_management_subscriptions')


class AzureEventGridEventSubscriptions(Base):
    __tablename__ = 'azure_event_grid_event_subscriptions'
    __table_args__ = (
        ForeignKeyConstraint(['azure_event_grid_domain_event_subscriptions'], ['dev.azure_event_grid_domains.id'], ondelete='SET NULL', name='azure_event_grid_event_subscri_4d3636d2e2e33fa9664169646aadcce0'),
        ForeignKeyConstraint(['azure_event_grid_domain_topic_event_subscriptions'], ['dev.azure_event_grid_domain_topics.id'], ondelete='SET NULL', name='azure_event_grid_event_subscri_564b4eb07b858f5aa07740f048a58df0'),
        ForeignKeyConstraint(['azure_event_grid_partner_topic_event_subscriptions'], ['dev.azure_event_grid_partner_topics.id'], ondelete='SET NULL', name='azure_event_grid_event_subscri_20cbdf1fbc9df6c6be8e2b4d8c13449d'),
        ForeignKeyConstraint(['azure_event_grid_system_topic_event_subscriptions'], ['dev.azure_event_grid_system_topics.id'], ondelete='SET NULL', name='azure_event_grid_event_subscri_ab9f6da7ae0e0299ec84e0f438e887c8'),
        ForeignKeyConstraint(['azure_event_grid_topic_event_subscriptions'], ['dev.azure_event_grid_topics.id'], ondelete='SET NULL', name='azure_event_grid_event_subscri_23f7dad1ad6870be79f7f439b8ca2626'),
        ForeignKeyConstraint(['resource_group_id'], ['dev.azure_resource_groups.id'], ondelete='CASCADE', name='azure_event_grid_event_subscri_ace2308ab9d0f2d88793d218cbc67a93'),
        PrimaryKeyConstraint('id', name='azure_event_grid_event_subscriptions_pkey'),
        Index('azureeventgrideventsubscription_name_resource_group_id', 'name', 'resource_group_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    destination: Mapped[str] = mapped_column(String)
    endpoint_type: Mapped[str] = mapped_column(String)
    delivery_schema: Mapped[str] = mapped_column(String)
    filter_subject_begins_with: Mapped[str] = mapped_column(String)
    filter_subject_ends_with: Mapped[str] = mapped_column(String)
    max_delivery_attempts: Mapped[int] = mapped_column(BigInteger)
    time_to_live_in_minutes: Mapped[int] = mapped_column(BigInteger)
    resource_group_id: Mapped[str] = mapped_column(String)
    azure_event_grid_domain_event_subscriptions: Mapped[Optional[str]] = mapped_column(String)
    azure_event_grid_domain_topic_event_subscriptions: Mapped[Optional[str]] = mapped_column(String)
    azure_event_grid_partner_topic_event_subscriptions: Mapped[Optional[str]] = mapped_column(String)
    azure_event_grid_system_topic_event_subscriptions: Mapped[Optional[str]] = mapped_column(String)
    azure_event_grid_topic_event_subscriptions: Mapped[Optional[str]] = mapped_column(String)

    azure_event_grid_domains: Mapped[Optional['AzureEventGridDomains']] = relationship('AzureEventGridDomains', back_populates='azure_event_grid_event_subscriptions')
    azure_event_grid_domain_topics: Mapped[Optional['AzureEventGridDomainTopics']] = relationship('AzureEventGridDomainTopics', back_populates='azure_event_grid_event_subscriptions')
    azure_event_grid_partner_topics: Mapped[Optional['AzureEventGridPartnerTopics']] = relationship('AzureEventGridPartnerTopics', back_populates='azure_event_grid_event_subscriptions')
    azure_event_grid_system_topics: Mapped[Optional['AzureEventGridSystemTopics']] = relationship('AzureEventGridSystemTopics', back_populates='azure_event_grid_event_subscriptions')
    azure_event_grid_topics: Mapped[Optional['AzureEventGridTopics']] = relationship('AzureEventGridTopics', back_populates='azure_event_grid_event_subscriptions')
    resource_group: Mapped['AzureResourceGroups'] = relationship('AzureResourceGroups', back_populates='azure_event_grid_event_subscriptions')


class AzureLogicAppIntegrationAccountAgreements(Base):
    __tablename__ = 'azure_logic_app_integration_account_agreements'
    __table_args__ = (
        ForeignKeyConstraint(['account_id'], ['dev.azure_logic_app_integration_accounts.id'], name='azure_logic_app_integration_ac_3ca6c917e98cb9a9f6e0826efe59876c'),
        ForeignKeyConstraint(['guest_partner_id'], ['dev.azure_logic_app_integration_account_partners.id'], name='azure_logic_app_integration_ac_79b0df3ee018d316ac58851e3f91ccd1'),
        ForeignKeyConstraint(['host_partner_id'], ['dev.azure_logic_app_integration_account_partners.id'], name='azure_logic_app_integration_ac_4f42d3b41cbf775a2e7f4bac8f409cef'),
        PrimaryKeyConstraint('id', name='azure_logic_app_integration_account_agreements_pkey'),
        Index('azurelogicappintegrationaccountagreement_name_type_account_id', 'name', 'type', 'account_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    account_id: Mapped[str] = mapped_column(String)
    host_partner_id: Mapped[str] = mapped_column(String)
    guest_partner_id: Mapped[str] = mapped_column(String)

    account: Mapped['AzureLogicAppIntegrationAccounts'] = relationship('AzureLogicAppIntegrationAccounts', back_populates='azure_logic_app_integration_account_agreements')
    guest_partner: Mapped['AzureLogicAppIntegrationAccountPartners'] = relationship('AzureLogicAppIntegrationAccountPartners', foreign_keys=[guest_partner_id], back_populates='azure_logic_app_integration_account_agreements')
    host_partner: Mapped['AzureLogicAppIntegrationAccountPartners'] = relationship('AzureLogicAppIntegrationAccountPartners', foreign_keys=[host_partner_id], back_populates='azure_logic_app_integration_account_agreements_')


class AzureLogicAppIntegrationAccountPartnerIdentities(Base):
    __tablename__ = 'azure_logic_app_integration_account_partner_identities'
    __table_args__ = (
        ForeignKeyConstraint(['partner_id'], ['dev.azure_logic_app_integration_account_partners.id'], name='azure_logic_app_integration_ac_1decba7840b70a404ead2e3df655b6b8'),
        PrimaryKeyConstraint('id', name='azure_logic_app_integration_account_partner_identities_pkey'),
        Index('azurelogicappintegrationaccoun_82a676cf2e57ddeecc11365b8a21a429', 'qualifier', 'partner_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    qualifier: Mapped[str] = mapped_column(String)
    value: Mapped[str] = mapped_column(String)
    partner_id: Mapped[str] = mapped_column(String)

    partner: Mapped['AzureLogicAppIntegrationAccountPartners'] = relationship('AzureLogicAppIntegrationAccountPartners', back_populates='azure_logic_app_integration_account_partner_identities')


class AzureLogicAppIntegrationAccountPartnerMetadata(Base):
    __tablename__ = 'azure_logic_app_integration_account_partner_metadata'
    __table_args__ = (
        ForeignKeyConstraint(['partner_id'], ['dev.azure_logic_app_integration_account_partners.id'], name='azure_logic_app_integration_ac_ac3319ed0ae9e5702429bb4e9b6d8646'),
        PrimaryKeyConstraint('id', name='azure_logic_app_integration_account_partner_metadata_pkey'),
        Index('azurelogicappintegrationaccountpartnermetadata_key_partner_id', 'key', 'partner_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    key: Mapped[str] = mapped_column(String)
    value: Mapped[str] = mapped_column(String)
    partner_id: Mapped[str] = mapped_column(String)

    partner: Mapped['AzureLogicAppIntegrationAccountPartners'] = relationship('AzureLogicAppIntegrationAccountPartners', back_populates='azure_logic_app_integration_account_partner_metadata')


class AzureServiceBusAuthorizationRules(Base):
    __tablename__ = 'azure_service_bus_authorization_rules'
    __table_args__ = (
        ForeignKeyConstraint(['namespace_id'], ['dev.azure_service_bus_namespaces.id'], ondelete='SET NULL', name='azure_service_bus_authorizatio_dd0ae64deedeaeeb99ed076850e2b03d'),
        ForeignKeyConstraint(['queue_id'], ['dev.azure_service_bus_queues.id'], ondelete='SET NULL', name='azure_service_bus_authorizatio_5a19e560ff5857ff96d1779b75ee2362'),
        ForeignKeyConstraint(['topic_id'], ['dev.azure_service_bus_topics.id'], ondelete='SET NULL', name='azure_service_bus_authorizatio_851857a8057da0e24a0dc303ed0f6704'),
        PrimaryKeyConstraint('id', name='azure_service_bus_authorization_rules_pkey'),
        Index('azureservicebusauthorizationru_8248cf319bad119c70c59c6204962cc9', 'name', 'namespace_id', 'queue_id', 'topic_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    manage: Mapped[Optional[bool]] = mapped_column(Boolean)
    send: Mapped[Optional[bool]] = mapped_column(Boolean)
    listen: Mapped[Optional[bool]] = mapped_column(Boolean)
    namespace_id: Mapped[Optional[str]] = mapped_column(String)
    queue_id: Mapped[Optional[str]] = mapped_column(String)
    topic_id: Mapped[Optional[str]] = mapped_column(String)

    namespace: Mapped[Optional['AzureServiceBusNamespaces']] = relationship('AzureServiceBusNamespaces', back_populates='azure_service_bus_authorization_rules')
    queue: Mapped[Optional['AzureServiceBusQueues']] = relationship('AzureServiceBusQueues', back_populates='azure_service_bus_authorization_rules')
    topic: Mapped[Optional['AzureServiceBusTopics']] = relationship('AzureServiceBusTopics', back_populates='azure_service_bus_authorization_rules')


class AzureServiceBusTopicSubscriptions(Base):
    __tablename__ = 'azure_service_bus_topic_subscriptions'
    __table_args__ = (
        ForeignKeyConstraint(['topic_id'], ['dev.azure_service_bus_topics.id'], name='azure_service_bus_topic_subscr_956e261e282023db9ed2e90f9a9f40c1'),
        PrimaryKeyConstraint('id', name='azure_service_bus_topic_subscriptions_pkey'),
        Index('azureservicebustopicsubscription_name_topic_id', 'name', 'topic_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    lock_duration: Mapped[str] = mapped_column(String)
    session_handling: Mapped[bool] = mapped_column(Boolean)
    default_time_to_live: Mapped[str] = mapped_column(String)
    delete_on_idle: Mapped[str] = mapped_column(String)
    max_delivery_count: Mapped[int] = mapped_column(BigInteger)
    message_count: Mapped[int] = mapped_column(BigInteger)
    message_active_count: Mapped[int] = mapped_column(BigInteger)
    message_scheduled_count: Mapped[int] = mapped_column(BigInteger)
    message_transfer_count: Mapped[int] = mapped_column(BigInteger)
    message_forward_to: Mapped[str] = mapped_column(String)
    dead_letter_forward_to: Mapped[str] = mapped_column(String)
    dead_letter_expired: Mapped[bool] = mapped_column(Boolean)
    dead_letter_count: Mapped[int] = mapped_column(BigInteger)
    dead_letter_transfer_count: Mapped[int] = mapped_column(BigInteger)
    topic_id: Mapped[str] = mapped_column(String)
    created_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    created_by: Mapped[Optional[str]] = mapped_column(String)
    changed_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))
    changed_by: Mapped[Optional[str]] = mapped_column(String)
    accessed_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))

    topic: Mapped['AzureServiceBusTopics'] = relationship('AzureServiceBusTopics', back_populates='azure_service_bus_topic_subscriptions')
    azure_service_bus_topic_subscription_rules: Mapped[List['AzureServiceBusTopicSubscriptionRules']] = relationship('AzureServiceBusTopicSubscriptionRules', back_populates='subscription')


class ProIntegratedConfigurationInterfaces(Base):
    __tablename__ = 'pro_integrated_configuration_interfaces'
    __table_args__ = (
        ForeignKeyConstraint(['pro_integrated_configuration_interface_channel'], ['dev.pro_communication_channels.id'], ondelete='SET NULL', name='pro_integrated_configuration_i_c18029d8ebbcc0ab9c3491341a967131'),
        ForeignKeyConstraint(['receiver_id'], ['dev.pro_integrated_configuration_receivers.id'], ondelete='CASCADE', name='pro_integrated_configuration_i_477fe89931ff94cf000742eb91e64ee0'),
        PrimaryKeyConstraint('id', name='pro_integrated_configuration_interfaces_pkey'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    operation: Mapped[str] = mapped_column(String)
    interface: Mapped[str] = mapped_column(String)
    interface_namespace: Mapped[str] = mapped_column(String)
    mapping: Mapped[str] = mapped_column(String)
    mapping_namespace: Mapped[str] = mapped_column(String)
    receiver_id: Mapped[str] = mapped_column(String)
    pro_integrated_configuration_interface_channel: Mapped[Optional[str]] = mapped_column(String)

    pro_communication_channels: Mapped[Optional['ProCommunicationChannels']] = relationship('ProCommunicationChannels', back_populates='pro_integrated_configuration_interfaces')
    receiver: Mapped['ProIntegratedConfigurationReceivers'] = relationship('ProIntegratedConfigurationReceivers', back_populates='pro_integrated_configuration_interfaces')
    pro_integrated_configuration_rules: Mapped[List['ProIntegratedConfigurationRules']] = relationship('ProIntegratedConfigurationRules', back_populates='pro_integrated_configuration_interfaces')


class AzureApiManagementApiOperationReplies(Base):
    __tablename__ = 'azure_api_management_api_operation_replies'
    __table_args__ = (
        ForeignKeyConstraint(['operation_id'], ['dev.azure_api_management_api_operations.id'], name='azure_api_management_api_opera_e054cf9ddea51ba8f55679ccaace746c'),
        PrimaryKeyConstraint('id', name='azure_api_management_api_operation_replies_pkey'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    status_code: Mapped[int] = mapped_column(BigInteger)
    operation_id: Mapped[str] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)

    operation: Mapped['AzureApiManagementApiOperations'] = relationship('AzureApiManagementApiOperations', back_populates='azure_api_management_api_operation_replies')
    azure_api_management_api_operation_parameters: Mapped[List['AzureApiManagementApiOperationParameters']] = relationship('AzureApiManagementApiOperationParameters', back_populates='response')


class AzureApiManagementPolicyProperties(Base):
    __tablename__ = 'azure_api_management_policy_properties'
    __table_args__ = (
        ForeignKeyConstraint(['policy_id'], ['dev.azure_api_management_policies.id'], name='azure_api_management_policy_pr_2c87d01eb2c0f2d2da8da95fdada098f'),
        PrimaryKeyConstraint('id', name='azure_api_management_policy_properties_pkey'),
        Index('azureapimanagementpolicyproperty_type_name_value_policy_id', 'type', 'name', 'value', 'policy_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    value: Mapped[str] = mapped_column(String)
    policy_id: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)

    policy: Mapped['AzureApiManagementPolicies'] = relationship('AzureApiManagementPolicies', back_populates='azure_api_management_policy_properties')


class AzureServiceBusTopicSubscriptionRules(Base):
    __tablename__ = 'azure_service_bus_topic_subscription_rules'
    __table_args__ = (
        ForeignKeyConstraint(['subscription_id'], ['dev.azure_service_bus_topic_subscriptions.id'], name='azure_service_bus_topic_subscr_76d295650195e90fab87ee5a2d80100d'),
        PrimaryKeyConstraint('id', name='azure_service_bus_topic_subscription_rules_pkey'),
        Index('azureservicebustopicsubscriptionrule_name_subscription_id', 'name', 'subscription_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    name: Mapped[str] = mapped_column(String)
    subscription_id: Mapped[str] = mapped_column(String)
    correlation_filter: Mapped[Optional[bytes]] = mapped_column(LargeBinary)
    sql_expression: Mapped[Optional[str]] = mapped_column(String)

    subscription: Mapped['AzureServiceBusTopicSubscriptions'] = relationship('AzureServiceBusTopicSubscriptions', back_populates='azure_service_bus_topic_subscription_rules')


class ProIntegratedConfigurationRules(Base):
    __tablename__ = 'pro_integrated_configuration_rules'
    __table_args__ = (
        ForeignKeyConstraint(['pro_integrated_configuration_interface_rules'], ['dev.pro_integrated_configuration_interfaces.id'], ondelete='SET NULL', name='pro_integrated_configuration_r_fce77e6a4e54fe4e186c1a23c9791ad6'),
        ForeignKeyConstraint(['pro_integrated_configuration_receiver_rules'], ['dev.pro_integrated_configuration_receivers.id'], ondelete='CASCADE', name='pro_integrated_configuration_r_7fc5bffc518e41fa16ea425f901b552c'),
        PrimaryKeyConstraint('id', name='pro_integrated_configuration_rules_pkey'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    operator: Mapped[str] = mapped_column(String)
    left_kind: Mapped[str] = mapped_column(String)
    left_value: Mapped[str] = mapped_column(String)
    left_type: Mapped[str] = mapped_column(String)
    right_kind: Mapped[str] = mapped_column(String)
    right_value: Mapped[str] = mapped_column(String)
    right_type: Mapped[str] = mapped_column(String)
    pro_integrated_configuration_interface_rules: Mapped[Optional[str]] = mapped_column(String)
    pro_integrated_configuration_receiver_rules: Mapped[Optional[str]] = mapped_column(String)

    pro_integrated_configuration_interfaces: Mapped[Optional['ProIntegratedConfigurationInterfaces']] = relationship('ProIntegratedConfigurationInterfaces', back_populates='pro_integrated_configuration_rules')
    pro_integrated_configuration_receivers: Mapped[Optional['ProIntegratedConfigurationReceivers']] = relationship('ProIntegratedConfigurationReceivers', back_populates='pro_integrated_configuration_rules')


class AzureApiManagementApiOperationParameters(Base):
    __tablename__ = 'azure_api_management_api_operation_parameters'
    __table_args__ = (
        ForeignKeyConstraint(['operation_id'], ['dev.azure_api_management_api_operations.id'], ondelete='SET NULL', name='azure_api_management_api_opera_48a84d86046cd0115c8fc7035347cbfe'),
        ForeignKeyConstraint(['response_id'], ['dev.azure_api_management_api_operation_replies.id'], ondelete='SET NULL', name='azure_api_management_api_opera_028876d7b108db11357d4e128c366e47'),
        PrimaryKeyConstraint('id', name='azure_api_management_api_operation_parameters_pkey'),
        Index('azureapimanagementapioperation_faab810827ee13c1b467548fd0e42c12', 'type', 'name', 'operation_id', 'response_id'),
        {'schema': 'dev'}
    )

    id: Mapped[str] = mapped_column(String, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    change_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    type: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    kind: Mapped[str] = mapped_column(String)
    values: Mapped[bytes] = mapped_column(LargeBinary)
    default_value: Mapped[Optional[str]] = mapped_column(String)
    operation_id: Mapped[Optional[str]] = mapped_column(String)
    response_id: Mapped[Optional[str]] = mapped_column(String)

    operation: Mapped[Optional['AzureApiManagementApiOperations']] = relationship('AzureApiManagementApiOperations', back_populates='azure_api_management_api_operation_parameters')
    response: Mapped[Optional['AzureApiManagementApiOperationReplies']] = relationship('AzureApiManagementApiOperationReplies', back_populates='azure_api_management_api_operation_parameters')

