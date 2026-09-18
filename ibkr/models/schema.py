from typing import Any, Literal

from pydantic import BaseModel, Field

from ibkr.models.enums import (
    AccountTypeEnum,
    AssetClassEnum,
    BaseCurrencyEnum,
    BrokerageServiceCodeEnum,
    CapabilityEnum,
    CardColorEnum,
    ControllingPersonDesignationEnum,
    CountryEnum,
    CustomerTypeEnum,
    EntityTypeEnum,
    ExchangeEnum,
    ExplanationTypeEnum,
    FormationTypeEnum,
    GenderEnum,
    InvestiveObjectiveEnum,
    IRATypeEnum,
    MaritalStatusEnum,
    NameSuffixEnum,
    OECDStatusEnum,
    PhoneTypeEnum,
    ProductTypeEnum,
    ProhibitedQuestionnaireDetailCodeEnum,
    QISubTypeEnum,
    RelationshipEnum,
    SalutationEnum,
    SignatureTypeEnum,
    TaxAuthorityEnum,
    TINTypeEnum,
    TitleCodeEnum,
)


class TaxResidency(BaseModel):
    country: str
    tin: str
    tinType: TINTypeEnum


class ACHDetails(BaseModel):
    custInitAch: bool
    bankName: str


class AUSExposureDetailsType(BaseModel):
    ausExposureRelationship: str
    personName: str
    licenseNumber: int


class AbandonAccount(BaseModel):
    accountId: str


class AccountConfigurationType(BaseModel):
    type: str
    value: bool


class TradingPermission(BaseModel):
    assetClass: AssetClassEnum
    exchangeGroup: str
    country: CountryEnum
    product: ProductTypeEnum


class CommissionConfig(BaseModel):
    style: Literal["Bundled", "Unbundled"]
    type: Literal["Commodities", "Securities"]


class ExchangeAccess(BaseModel):
    assetClass: AssetClassEnum
    exchange: ExchangeEnum


class DVPInstruction(BaseModel):
    id: str
    externalId: str
    externalAccountID: str
    accountID: str
    name: str
    type: Literal["DTCID", "NSCC", "CMTA", "GUS", "OCCSSF"]
    role: Literal["E", "C", "B"]
    agentID: str
    firmID: str
    agentName: str
    accountName: str
    dayDoID: str
    txGroupCode: Literal["G", "Z", "R", "N"]
    brokerCode: str
    assetClass: AssetClassEnum
    exchange: ExchangeEnum
    prepayTax: bool
    prepayCommission: bool
    expiry: str
    default: bool


class OrderValueLimits(BaseModel):
    maxOrderValue: float
    maxGrossValue: float
    maxNetValue: float
    netContractLimit: float


class EFPQuantityLimits(BaseModel):
    maxNominalEfpPerOrder: int
    maxNetEfpTrades: int
    maxGrossEfpTrades: int


class OrderQuantityLimit(BaseModel):
    asset: AssetClassEnum
    quantity: int


class DayQuantityLimit(BaseModel):
    asset: AssetClassEnum
    quantity: int


class TradingLimits(BaseModel):
    orderValueLimits: OrderValueLimits
    efpQuantityLimits: EFPQuantityLimits
    orderQuantityLimits: list[OrderQuantityLimit]
    dayQuantityLimits: list[DayQuantityLimit]


class MarkupStaircaseType(BaseModel):
    amount: float
    break_amount: float = Field(alias="break")


class CommissionMarkupType(BaseModel):
    stairs: list[MarkupStaircaseType]
    code: str
    minimum: float
    maximum: float
    type: Literal["FA", "FM", "PM"]
    amount: float
    plusCost: bool
    ticketCharge: float


class CommissionScheduleType(BaseModel):
    markups: list[CommissionMarkupType]
    pricingStructure: Literal["FIXED", "TIERED"]


class AnnualBlendedPercentage(BaseModel):
    blendedFrom: str
    blendedTo: str
    percentage: str


class NAVRangeType(BaseModel):
    min: float
    max: float
    maxFee: float


class AutomatedWrapFeeDetailsType(BaseModel):
    perTradeMarkups: CommissionScheduleType
    annualBlendedPercentages: list[AnnualBlendedPercentage]
    navRanges: list[NAVRangeType]
    type: Literal[
        "ANNUALFLATFEE",
        "ANNUALFLATFEE_MONTHLY",
        "ANNUALFLATFEE_QUATERLY",
        "PERCENTOFEQUITY",
        "PERCENTOFEQUITY_MONTHLY",
        "PERCENTOFEQUITY_EOM",
        "PERCENTOFEQUITY_QUATERLY",
        "PERCENTOFEQUITY_QUARTERLY",
        "PERCENTOFEQUITY_EOQ",
        "BLENDEDPERCENTOFEQUITY",
        "BLENDEDPERCENTOFEQUITY_MONTHLY",
        "BLENDEDPERCENTOFEQUITY_EOM",
        "BLENDEDPERCENTOFEQUITY_QUARTERLY",
        "BLENDEDPERCENTOFEQUITY_EOQ",
        "INVOICE_LIMIT",
        "INVOICE_LIMIT_Q",
        "PERCENTOFPROFIT",
        "PERCENTOFPROFIT_QUARTER",
        "PERTRADE",
        "PERCENTOFNLV_CAP",
        "PERCENTOFNLV_CAP_EOPEQTY",
        "PERCENTOFNLV_CAP_Q",
        "PERCENTOFNLV_CAP_EOPEQTY_Q",
    ]
    maxFee: float
    numContracts: int
    postFrequency: str
    percentOfNLVCap: str
    percentOfNLVCapQ: str


class HighWaterMarkConfigurationType(BaseModel):
    numberOfPeriods: int
    prorateForWithdrawals: bool


class PreviousLossesType(BaseModel):
    loss: int
    quarter: int
    year: int
    currency: str


class HighWaterMarkType(BaseModel):
    hwm: HighWaterMarkConfigurationType
    previousLosses: list[PreviousLossesType]


class AdvisorWrapFeesType(BaseModel):
    automatedFeesDetails: list[AutomatedWrapFeeDetailsType]
    highWaterMarkConfigHwma: HighWaterMarkType
    highWaterMarkConfigHwmq: HighWaterMarkType
    strategy: Literal["AUTOMATED", "DIRECTBILLING", "NO_FEE"]
    chargeAdvisor: bool
    chargeOtherFeesToAdvisor: bool


class InterestMarkupSchedule(BaseModel):
    currency: BaseCurrencyEnum
    debitMarkup: float
    ibDebitMarkup: float
    creditMarkdown: float
    shortCreditMarkdown: float
    shortCfdCreditMarkdown: float
    longCfdDebitMarkdown: float
    shortIndexCfdCreditMarkdown: float
    longIndexCfdDebitMarkdown: float
    shortFxCfdMarkup: float
    longFxCfdMarkdown: float


class IndividualName(BaseModel):
    salutation: SalutationEnum
    first: str
    last: str
    middle: str
    suffix: NameSuffixEnum
    title: str


class Address(BaseModel):
    street1: str
    street2: str
    city: str
    state: str
    country: str
    postalCode: str


class ResidenceAddress(Address):
    description: str


class PhoneInfo(BaseModel):
    type: PhoneTypeEnum
    number: str
    country: str
    verified: bool


class Identification(BaseModel):
    description: str
    citizenship: str
    citizenship2: str
    citizenship3: str
    ssn: str
    sin: str
    driversLicense: str
    passport: str
    alienCard: str | None
    hkTravelPermit: str | None
    medicareCard: str | None
    cardColor: CardColorEnum | None
    medicareReference: str
    nationalCard: str | None
    issuingCountry: str | None
    issuingState: str | None
    rta: str | None
    legalResidenceCountry: str | None
    legalResidenceState: str | None
    educationalQualification: str | None
    fathersName: str | None
    greenCard: bool | None
    panNumber: str | None
    taxId: str | None
    proofOfAgeCard: str | None
    expire: bool | None
    expirationDate: str


class EmploymentDetails(BaseModel):
    employer: str
    occupation: str
    description: str
    employerBusiness: str
    employerAddress: Address
    employerPhone: str
    emplCountryResCountryDetails: str
    businessDescription: str


class LocalTaxForm(BaseModel):
    taxAuthority: TaxAuthorityEnum | None
    qualified: bool
    treatyCountry: str


class FormW9(BaseModel):
    localTaxForms: list[LocalTaxForm]
    name: str
    businessName: str
    customerType: CustomerTypeEnum
    taxClassification: str
    otherCustomerType: str
    tin: str
    tinType: TINTypeEnum
    cert1: bool
    cert2: bool
    cert3: bool
    cert4: bool
    signatureType: SignatureTypeEnum
    blankForm: bool
    taxFormFile: str
    proprietaryFormNumber: int


class FormW8BEN(BaseModel):
    localTaxForms: list[LocalTaxForm]
    name: str
    tin: str
    foreignTaxId: str
    tinOrExplanationRequired: bool
    explanation: ExplanationTypeEnum
    referenceNumber: int
    part29ACountry: str
    cert: bool
    signatureType: SignatureTypeEnum
    blankForm: bool
    taxFormFile: str
    proprietaryFormNumber: int
    electronicFormat: bool
    submitDate: str


class FormCRS(BaseModel):
    controllingPersonDesignation: ControllingPersonDesignationEnum
    oecdStatus: OECDStatusEnum


class ProhibitedQuestionnaireDetail(BaseModel):
    code: ProhibitedQuestionnaireDetailCodeEnum
    status: bool
    details: str


class ProhibitedCountryQuestionnaireList(BaseModel):
    prohibitedQuestionnaireDetail: list[ProhibitedQuestionnaireDetail]
    accountId: str
    externalId: str
    entityId: str


class Individual(BaseModel):
    name: IndividualName
    nativeName: IndividualName
    birthName: IndividualName
    motherMaidenName: IndividualName
    dateOfBirth: str
    countryOfBirth: str
    cityOfBirth: str
    gende: GenderEnum
    maritalStatus: MaritalStatusEnum
    numDependents: int
    residenceAddress: ResidenceAddress
    mailingAddress: Address
    phones: list[PhoneInfo]
    email: str
    identification: Identification
    employmentType: str
    employmentDetails: EmploymentDetails
    employeeTitle: str
    taxResidencies: list[TaxResidency]
    w9: FormW9
    w8Ben: FormW8BEN
    crs: FormCRS
    prohibitedCountryQuestionnaire: ProhibitedCountryQuestionnaireList
    id: str
    externalId: str
    userId: str
    sameMailAddress: bool
    authorizedToSignOnBehalfOfOwner: bool
    authorizedTrader: bool
    usTaxResident: bool
    translated: bool
    primaryTrustee: bool


class LegalEntityIdentification(BaseModel):
    placeOfBusinessAddress: Address
    mailingAddress: Address
    identification: str
    identificationCountry: str
    formationCountry: str
    formationType: FormationTypeEnum
    exchangeCode: str
    exchangeSymbol: str
    sameMailAddress: bool


class LegalEntity(BaseModel):
    name: str
    address: Address
    phones: list[PhoneInfo]
    email: str
    legalEntityIdentification: LegalEntityIdentification
    taxResidencies: list[TaxResidency]
    id: str
    externalId: str
    usTaxResident: bool
    translated: bool


class CustodianType(BaseModel):
    individual: Individual
    legalEntity: LegalEntity
    employee: Individual


class RepDetail(BaseModel):
    repId: str
    percentage: int


class AccountRep(BaseModel):
    repDetails: list[RepDetail]
    included: bool


class Title(BaseModel):
    value: str
    code: TitleCodeEnum


class IRAPrimaryBeneficiary(BaseModel):
    name: IndividualName
    nativeName: IndividualName
    birthName: IndividualName
    motherMaidenName: IndividualName
    dateOfBirth: str
    countryOfBirth: str
    cityOfBirth: str
    gender: GenderEnum
    maritalStatus: MaritalStatusEnum
    numDependents: int
    residenceAddress: ResidenceAddress
    mailingAddress: Address
    phones: list[PhoneInfo]
    email: str
    identification: Identification
    employmentType: str
    employmentDetails: EmploymentDetails
    employeeTitle: str
    taxResidencies: list[TaxResidency]
    w9: FormW9
    w8Ben: FormW8BEN
    crs: FormCRS
    prohibitedCountryQuestionnaire: ProhibitedCountryQuestionnaireList
    id: str
    externalId: str
    userId: str
    sameMailAddress: bool
    authorizedToSignOnBehalfOfOwner: bool
    authorizedTrader: bool
    usTaxResident: bool
    translated: bool
    primaryTrustee: bool
    ownershipPercentage: float
    title: Title
    relationship: RelationshipEnum


class IRAPrimaryBeneficiaryEntity(BaseModel):
    name: str
    address: Address
    id: str
    externalId: str
    ownershipPercentage: str
    title: Title
    relationship: RelationshipEnum
    executor: Individual
    executionDate: str
    articleOfWill: str
    entityType: EntityTypeEnum
    charityNumber: str


class IRAContingentBeneficiary(BaseModel):
    pass


class IRAContingentBeneficiaryEntity(BaseModel):
    pass


class IRABeneficiariesType(BaseModel):
    primaryBeneficiaries: list[IRAPrimaryBeneficiary]
    primaryBeneficiaryEntities: list[IRAPrimaryBeneficiaryEntity]
    contingentBeneficiaries: list[IRAContingentBeneficiary]
    contingentBeneficiaryEntities: list[IRAContingentBeneficiaryEntity]
    spousePrimaryBeneficary: bool
    successor: bool


class IRADecedent(BaseModel):
    pass


class DepositNotification(BaseModel):
    pass


class Account(BaseModel):
    accountConfiguration: AccountConfigurationType
    investmentObjectives: list[InvestiveObjectiveEnum]
    brokerageServiceCodes: list[BrokerageServiceCodeEnum]
    capabilities: list[CapabilityEnum]
    optionLevel: int
    tradingPermissions: list[TradingPermission]
    commissionConfigs: list[CommissionConfig]
    allExchangeAccess: list[ExchangeAccess]
    dvpInstructions: list[DVPInstruction]
    tradingLimits: TradingLimits
    advisorWrapFees: AdvisorWrapFeesType
    feesTemplateName: str
    clientCommissionSchedule: CommissionScheduleType
    clientInterestMarkupSchedules: list[InterestMarkupSchedule]
    decendent: IRADecedent
    iraBeneficiaries: IRABeneficiariesType
    extPositionsTransfers: list
    depositNotification: DepositNotification
    custodian: CustodianType
    successorCustodian: CustodianType
    accountRep: AccountRep
    id: str
    externalId: str
    propertyProfile: str
    baseCurrency: BaseCurrencyEnum
    employeePlan: str
    multiCurrency: bool
    migration: bool
    sourceAccountId: str
    margin: str
    ira: bool
    iraType: IRATypeEnum
    iraOfficialTitle: str
    clientActiveTrading: bool
    duplicate: bool
    numberOfDuplicates: int
    stockYieldProgram: bool
    alias: str
    accountType: AccountTypeEnum
    drip: bool
    qiSubType: QISubTypeEnum


class AccountClose(BaseModel):
    accountId: str
    closeReason: str


class AccountConfiguration(BaseModel):
    accountId: str
    type: str
    value: bool


class AccountData(BaseModel):
    accountId: str
    masterAccountId: str
    mainAccount: str
    sourceAccountId: str
    primaryUser: str
    clearingStatus: str
    clearingStatusDescription: str
    stateCode: str
    optionLevel: int
    baseCurrency: BaseCurrencyEnum
    dateBegun: str
    dateApproved: str
    dateOpened: str
    dateFunded: str
    dateClosed: str
    dateLinked: str
    dateDelinked: str
    accountTitle: str
    officialTitle: str
    accountAlias: str
    emailAddress: str
    margin: str
    applicantType: str
    subType: str
    stockYieldProgram: dict[Any, str]
    feeTemplate: dict[Any, str]
    capabilities: dict[Any, list[str]]
    limitedOptionTrading: str
    investmentObjectives: list[str]
    dividendReinvestment: dict[Any, bool]
    externalId: str
    mifidCategory: str
    mifirStatus: str
    equity: float
    household: str
    propertyProfile: str
    processType: str
    riskScore: int
    class_action_program: str
    trustType: str
    orgType: str
    businessDescription: str
    usTaxPurposeType: str
    tradeIntentionType: str
    registeredAddress: dict[Any, str]
    mailing: dict[Any, str]
    countryOfCorporation: str
    lei: str
    taxIds: list[dict[Any, str]]
    taxTreatyDetails: list[dict[Any, str]]
    signatures: list[str]


class ErrorResponse(BaseModel):
    status: int
    error: str
    message: str


class AssociatedPerson(BaseModel):
    pass


class AssociatedEntity(BaseModel):
    pass


class IndividualIRABene(BaseModel):
    pass


class EntityIRABene(BaseModel):
    pass


class RestrictionInfo(BaseModel):
    pass


class AccountDetailsResponse(BaseModel):
    error: ErrorResponse
    hasError: bool
    errorDescription: str
    account: AccountData
    associatedPersons: list[AssociatedPerson]
    associatedEntities: list[AssociatedEntity]
    withHoldingStatement: dict[Any, str]
    marketData: list[Any]
    financialInformation: dict[Any, Any]
    sourcesOfWealth: list[Any]
    tradeBundles: list[str]
    individualIRABeneficiaries: list[IndividualIRABene]
    entityIRABeneficiaries: list[EntityIRABene]
    decedents: list[Any]
    restrictions: list[RestrictionInfo]
