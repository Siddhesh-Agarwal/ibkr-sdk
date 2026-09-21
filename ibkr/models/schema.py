from typing import Any, Literal

from pydantic import BaseModel, EmailStr, Field

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
    DepositNotificationTypeEnum,
    EntityTypeEnum,
    ExchangeEnum,
    ExplanationTypeEnum,
    FATCACompliantTypeEnum,
    FATCAStatusEnum,
    FeeDetailsTypeEnum,
    FormationTypeEnum,
    GenderEnum,
    InvestiveObjectiveEnum,
    IRATypeEnum,
    KnowledgeLevelEnum,
    LanguageEnum,
    MaritalStatusEnum,
    NameSuffixEnum,
    OECDStatusEnum,
    OwnerTypeEnum,
    PhoneTypeEnum,
    ProductTypeEnum,
    ProhibitedQuestionnaireDetailCodeEnum,
    QISubTypeEnum,
    RegulatoryDetailCodeEnum,
    RelationshipEnum,
    SalutationEnum,
    SignatureTypeEnum,
    SourceOfIncomeTypeEnum,
    SourceOfWealthTypeEnum,
    TaxAuthorityEnum,
    TINTypeEnum,
    TitleCodeEnum,
    W9CustomerTypeEnum,
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
    type: FeeDetailsTypeEnum
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
    customerType: W9CustomerTypeEnum
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


class FormW8BENE(BaseModel):
    substantialUsOwnerExternalIds: list[str]
    name: str
    countryOfOrganization: str
    disregardedEntityName: str
    entityType: Literal[
        "CORPORATION",
        "DISREGARDED_ENTITY",
        "PARTNERSHIP",
        "SIMPLE_TRUST",
        "GRANTOR_TRUST",
        "COMPLEX_TRUST",
        "ESTATE",
        "GOVERNMENT",
        "CENTRAL_BANK_OF_ISSUE",
        "TAX_EXEMPT_ORGANIZATION",
        "PRIVATE_FOUNDATION",
    ]
    fatcaStatus: FATCAStatusEnum
    usTin: str
    giin: str
    foreignTin: str
    tinOrExplanationRequired: bool
    explanation: Literal[
        "US_TIN", "TIN_NOT_DISCLOSED", "TIN_NOT_REQUIRED", "TIN_NOT_ISSUED"
    ]
    referenceNumber: int
    submitDate: str
    box11Status: Literal[
        "LIMITED_BRANCH",
        "US_BRANCH",
        "PARTICIPATING_FFI",
        "REPORTING_MODEL_1_FFI",
        "REPORTING_MODEL_2_FFI",
    ]
    part314A: bool
    part314ACountry: str
    part314B: Literal[
        "CompanyMeetsOwnershipAndBaseErosionTest",
        "TaxExemptPensionTrustOrPensionFund",
        "CompanyMeetsDerivativeBenefitsTest",
        "TaxExemptOrganization",
        "CompanyWithIncomeActiveBusiness",
        "PubliclyTradedCorporation",
        "FavorableDiscretionaryDetermination",
        "SubsidiaryOfAPubliclyTradedCorporation",
        "Government",
        "NoLobArticleInTreaty",
        "Other",
    ]
    part314C: bool
    part416: str
    part417I: bool
    part417Ii: bool
    part518: bool
    part619: bool
    part720: str
    part721: bool
    part822: bool
    part923: bool
    part1024A: bool
    part1024B: bool
    part1024C: bool
    part1024D: bool
    part1125A: bool
    part1125B: bool
    part1125C: bool
    part1226: bool
    part1226Desc1: str
    part1226Desc2: str
    part1226Desc3: Literal[
        "CollectiveInvestmentVehicle",
        "ExemptBeneficialOwner-RetirementPlan",
        "FinancialInstitutionwithlocalClientBase",
        "InvestmentAdvisorsandManagers",
        "LocalBank",
        "SponsoredCloselyHeldInvestmentVehicle",
        "SponsoredInvestmentEntity",
        "TrusteeDocumentedTrust",
    ]
    part1226Desc4: str
    part1327: bool
    part1428A: bool
    part1428B: bool
    part1529A: bool
    part1529B: bool
    part1529C: bool
    part1529D: bool
    part1529E: bool
    part1529F: bool
    part1630: bool
    part1731: bool
    part1832: bool
    part1933: bool
    part2034: bool
    part2135: bool
    part2135Date: str
    part2236: bool
    part2337A: bool
    part2337ADesc: str
    part2337B: bool
    part2337BDesc1: str
    part2337BDesc2: str
    part2438: bool
    part2539: bool
    part2640A: bool
    part2640B: bool
    part2640C: bool
    part2741: bool
    part2842: str
    part2843: bool
    cert: bool
    signatureType: SignatureTypeEnum
    blankForm: bool
    taxFormFile: str
    proprietaryFormNumber: int
    electronicFormat: bool


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
    email: EmailStr
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
    email: EmailStr
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
    email: EmailStr
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
    email: EmailStr
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


class IRAContingentBeneficiaryEntity(BaseModel):
    name: str
    address: Address
    id: str
    externalId: str
    ownershipPercentage: float
    title: Title
    relationship: RelationshipEnum
    executor: Individual
    executionDate: str
    articleOfWill: str
    entityType: EntityTypeEnum


class IRABeneficiariesType(BaseModel):
    primaryBeneficiaries: list[IRAPrimaryBeneficiary]
    primaryBeneficiaryEntities: list[IRAPrimaryBeneficiaryEntity]
    contingentBeneficiaries: list[IRAContingentBeneficiary]
    contingentBeneficiaryEntities: list[IRAContingentBeneficiaryEntity]
    spousePrimaryBeneficary: bool
    successor: bool


class IRADecedent(BaseModel):
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
    email: EmailStr
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
    dateOfDeath: str
    title: Title
    inheritorType: Literal["S", "I", "T", "O"]
    relationship: RelationshipEnum


class CheckDetails(BaseModel):
    checkNumber: str
    routingNumber: str
    accountNumber: str


class WireDetails(BaseModel):
    bankName: str
    bankAccountNumber: str
    bankCode: str
    routingNumber: str
    instruction: str
    countryCode: str
    referenceNumber: str


class IRADepositDetails(BaseModel):
    depositType: Literal["contribution", "rollover"]
    taxYear: Literal["current", "prior"]
    fromIraType: IRATypeEnum


class DepositNotification(BaseModel):
    checkDetails: CheckDetails
    wireDetails: WireDetails
    achDetails: ACHDetails
    iraDepositDetails: IRADepositDetails
    type: DepositNotificationTypeEnum
    amount: float
    currency: BaseCurrencyEnum
    ibAccount: str


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
    emailAddress: EmailStr
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
    entityId: int
    externalCode: str
    firstName: str
    middleName: str
    middleInitial: str
    lastName: str
    suffix: str
    username: str
    passwordDate: str
    userStatus: str
    userStatusTrading: str
    lastLogin: str
    gender: str
    maritalStatus: str
    salutation: str
    ownershipPercentage: float
    email: EmailStr
    countryOfCitizenship: str
    countryOfBirth: str
    dateOfBirth: str
    motersMaidenName: str
    numberOfDependents: int
    securityDevice: str
    commercial: str
    countryOfLegalResidence: str
    stateOfLegalResidence: str
    mdSubscriberStatus: str
    phones: dict[Any, str]
    residence: dict[Any, str]
    mailing: dict[Any, str]
    identityDocuments: list[dict[Any, str]]
    associations: list[str]
    employmentType: str
    employmentDetails: dict[Any, str]
    subscribedServices: list[dict[Any, str]]
    taxTreatyDetails: list[dict[Any, str]]


class AssociatedEntity(BaseModel):
    entityId: int
    externalCode: str
    name: str
    email: EmailStr
    organizationCountry: str
    phones: dict[Any, str]
    residence: dict[Any, str]
    mailing: dict[Any, str]
    associations: list[str]
    identityDocuments: list[dict[Any, str]]
    taxTreatyDetails: list[dict[Any, str]]
    AssociatedPersons: list[AssociatedPerson]


class AssociatedEntities(BaseModel):
    associatedIndividuals: list[AssociatedPerson]
    associatedEntities: list[AssociatedEntity]


class IndividualIRABene(BaseModel):
    firstName: str
    lastName: str
    dateOfBirth: str
    type: str
    identification: dict[Any, str]
    location: dict[Any, str]
    relationship: str
    ownership: int
    perStripes: str


class EntityIRABene(BaseModel):
    name: str
    entityType: str
    type: str
    location: dict[Any, str]
    articleOfWill: str


class RestrictionInfo(BaseModel):
    id: int
    byIB: bool
    name: str


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


class UpdateExternalId(BaseModel):
    accountId: str
    newExternalId: str


class UpdatePropertyProfile(BaseModel):
    accountId: str
    propertyProfile: str


class UpdateAccountAlias(BaseModel):
    accountId: str
    accountAlias: str


class ChangeBaseCurrency(BaseModel):
    accountId: str
    newBaseCurrency: BaseCurrencyEnum


class UserDetails(BaseModel):
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
    phones: list[str]
    email: EmailStr
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
    title: list[Title]
    authorizedPerson: bool
    referenceUsername: str


class AddNewUser(BaseModel):
    accountId: str
    prefix: str
    userDetails: UserDetails
    userName: str
    inputLanguage: LanguageEnum
    translation: bool


class Service(BaseModel):
    value: int
    action: Literal["ADD", "REMOVE"]


class ManageMarketDataSubscriptions(BaseModel):
    service: Service
    referenceUserName: str


class AddLEVFXCapability(BaseModel):
    accountId: str


class AddMiFIRData(BaseModel):
    accountId: str
    title: str
    identifications: list[Identification]


class AttachedFileType(BaseModel):
    fileName: str
    fileLength: int
    sha1Checksum: str


class FilePayload(BaseModel):
    mimeType: str
    data: str


class Document(BaseModel):
    signedBy: list[str]
    attachedFile: AttachedFileType
    formNumber: int
    validAddress: bool | None
    execLoginTimestamp: int
    execTimestamp: int
    documentType: str | None
    signature: str | None
    externalAccountId: str | None
    externalIndividualId: str | None
    proofOfIdentityType: Literal[
        "Driver License",
        "Passport",
        "Alien ID Card",
        "National ID Card",
        "Bank Statement",
        "Evidence of Ownership of Property",
        "Credit Card Statement",
        "Utility Bill",
        "Brokerage Statement",
        "T4 Statement",
        "CRA Assessment",
        "Hong Kong and Macao Entry Permit",
    ]
    expirationDate: str
    proofOfAddressType: Literal[
        "Driver License",
        "Bank Statement",
        "Brokerage Statement",
        "Homeowner Insurance Policy Bill",
        "Homeowner Insurance Policy Document",
        "Renter Insurance Policy bill",
        "Renter Insurance Policy Document",
        "Security System Bill",
        "Government Issued Letters",
        "Utility Bill",
        "Current Lease",
        "Evidence of Ownership of Property",
        "Other Document",
    ]
    payload: FilePayload


class DocumentSubmission(BaseModel):
    documents: list[Document]
    accountId: str
    inputLanguage: LanguageEnum
    translation: bool


class AddTradingPermissions(BaseModel):
    tradingPermissions: list[TradingPermission]
    documentSubmission: DocumentSubmission
    accountId: str
    optionLevel: int


class RemoveTradingPermissions(BaseModel):
    tradingPermissions: list[TradingPermission]
    accountId: str


class ChangeMarginType(BaseModel):
    documentSubmission: DocumentSubmission
    accountId: str
    operation: str
    newMargin: str


class AddCLPCapability(BaseModel):
    accountId: str
    documents: list[Document]


class AssetExperience(BaseModel):
    assetClass: AssetClassEnum
    yearsTrading: int
    tradesPerYear: int
    knowledgeLevel: KnowledgeLevelEnum


class SourceOfIncomeType(BaseModel):
    sourceType: SourceOfIncomeTypeEnum
    percentage: int
    description: str


class SourceOfWealthType(BaseModel):
    sourceType: SourceOfWealthTypeEnum
    percentage: int
    usedForFunds: bool
    description: str


class SOIQuestionnaire(BaseModel):
    details: str


class QuestionnaireType(BaseModel):
    formNumber: int
    details: str


class FinancialInformation(BaseModel):
    investmentExperience: list[AssetExperience]
    investmentObjectives: list[InvestiveObjectiveEnum]
    additionalSourcesOfIncome: list[SourceOfIncomeType]
    sourcesOfWealth: list[SourceOfWealthType]
    soiQuestionnaire: SOIQuestionnaire
    questionnaires: list[QuestionnaireType]
    netWorth: float
    liquidNetWorth: float
    annualNetIncome: float
    totalAssets: float
    sourceOfFunds: str
    translated: bool


class ResetAbandonedAccount(BaseModel):
    accountId: str


class ChangeFinancialInformation(BaseModel):
    accountId: str
    referenceUserName: str
    newFinancialInformation: FinancialInformation


class UpdateEmail(BaseModel):
    email: EmailStr
    token: str
    access: bool
    externalId: str
    entityId: str


class UpdatePassword(BaseModel):
    encryptedPassword: str
    encryptedKeyName: str
    token: str


class UpdateCredentials(BaseModel):
    updateEmail: UpdateEmail
    updatePassword: UpdatePassword
    accountId: str
    referenceUserName: str


class RepresentativeDetail(BaseModel):
    representativeId: str
    percentage: int


class UpdateAccountRepresentatives(BaseModel):
    representativeDetails: list[RepresentativeDetail]
    accountId: str


class CompleteLoginMessage(BaseModel):
    loginMessageIds: list[int]
    accountId: str


class ReopenAccount(BaseModel):
    accountId: str


class EnrollInSYEP(BaseModel):
    accountId: str
    documents: list[Document]


class LeaveSYEP(BaseModel):
    accountId: str


class EnrollInDRIP(BaseModel):
    accountId: str


class LeaveDRIP(BaseModel):
    accountId: str


class DuplicateAccount(BaseModel):
    accountId: str
    numberOfDuplicates: int


class ProcessDocuments(BaseModel):
    documents: list[Document]
    inputLanguage: LanguageEnum
    translation: bool


class UpdateBCAN(BaseModel):
    accountId: str
    bcan: str
    ceNumber: str


class ProhibitedCountryQuestionnaire(BaseModel):
    prohibitedQuestionnaireDetails: list[ProhibitedQuestionnaireDetail]
    accountId: str
    externalId: str
    entityId: str


class UpdateWithholdingStatement(BaseModel):
    accountId: str
    fatcaCompliantType: FATCACompliantTypeEnum
    usIncomeTax: bool
    treatyCountry: str
    certW8Imy: bool
    effectiveDate: str


class QualifiedPurchaserDetail(BaseModel):
    code: Literal["InvestmentCompanyAct", "DiscretionaryBasis"]
    status: bool


class QualifiedPurchaser(BaseModel):
    qualifiedPurchaserDetails: list[QualifiedPurchaserDetail]
    status: bool


class EligibleContractParticipantDetail(BaseModel):
    code: Literal["DiscretionaryBasis", "HighRisk"]
    status: bool


class EligibleContractParticipant(BaseModel):
    eligibleContractParticipantDetails: list[EligibleContractParticipantDetail]
    status: bool


class AccreditedInvestor(BaseModel):
    qualifiedPurchaser: QualifiedPurchaser
    eligibleContractParticipant: EligibleContractParticipant
    signedBy: list[str]
    accountId: str
    status: bool
    signature: str


class AssociatedIndividual(BaseModel):
    name: IndividualName
    nativeName: IndividualName
    birthName: IndividualName
    motherMaidenName: IndividualName
    countryOfBirth: str
    cityOfBirth: str
    gender: GenderEnum
    maritalStatus: MaritalStatusEnum
    numDependents: int
    residenceAddress: ResidenceAddress
    mailingAddress: Address
    phones: list[PhoneInfo]
    email: EmailStr
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
    ownerType: OwnerTypeEnum
    ownershipPercentage: float
    titles: list[Title]
    authorizedPerson: bool
    referenceUsername: str


class ChangeAccountHolderDetail(BaseModel):
    newAccountHolderDetails: list[AssociatedIndividual]
    documents: DocumentSubmission
    accountId: str
    referenceUserName: str
    inputLanguage: str
    Enum: str
    Array: list[str]
    translation: bool


class UpdateUserAccessRights(BaseModel):
    subAccounts: list[str]
    repId: str
    action: str


class OrganizationIdentification(BaseModel):
    placeOfBusinessAddress: Address
    mailingAddress: Address
    phones: list[PhoneInfo]
    name: str
    businessDescription: str
    websiteAddress: str
    identification: str
    identificationCountry: str
    formationCountry: str
    formationState: str
    sameMailAddress: bool
    translated: bool


class RegulatoryDetail(BaseModel):
    code: RegulatoryDetailCodeEnum
    status: bool
    details: str
    detail: str
    externalIndividualId: str


class SelfRegulatedMembershipType(BaseModel):
    exchanges: str
    organizations: str


class AffiliationDetailsType(BaseModel):
    affiliationRelationship: Literal["Self", "Spouse", "Parent", "Child", "Other"]
    personName: str
    companyId: int
    company: str
    companyMailingAddress: Address
    companyPhone: str
    companyEmailAddress: EmailStr
    duplicateStmtRequired: bool


class PublicCompanyInfoType(BaseModel):
    exchangeTradedOn: str
    quotedSymbol: str


class ORGRegulatorType(BaseModel):
    regulatorName: str
    regulatorCountry: str
    regulatedInCapacity: str
    regulatorId: str


class ORGRegulatoryInfoType(BaseModel):
    publicCompanyInfo: PublicCompanyInfoType
    orgRegulators: list[ORGRegulatorType]
    regulated: bool
    public: bool


class PoliticalMilitaryDiplomaticDetailsType(BaseModel):
    personName: str
    title: str
    organization: str
    country: str


class RegulatoryInformation(BaseModel):
    regulatoryDetails: list[RegulatoryDetail]
    regulatoryDetail: list[RegulatoryDetail]
    selfRegulatedMembership: SelfRegulatedMembershipType
    affiliationDetails: AffiliationDetailsType
    financialOrgTypes: list[str]
    orgRegulatoryInfo: ORGRegulatoryInfoType
    ausExposureDetails: AUSExposureDetailsType
    controllerExchangeCode: str
    politicalMilitaryDiplomaticDetails: PoliticalMilitaryDiplomaticDetailsType
    translated: bool


class Organization(BaseModel):
    identification: OrganizationIdentification
    regulatoryInformation: RegulatoryInformation
    associatedEntities: AssociatedEntities


class AddRelationship(BaseModel):
    name: str
    ownershipPercentage: int


class AddEntity(BaseModel):
    addRelationships: list[AddRelationship]
    individual: Individual
    legalEntity: LegalEntity
    organization: Organization
    documents: list[Document]


class TrustIdentification(BaseModel):
    address: Address
    mailingAddress: Address
    phones: list[PhoneInfo]
    name: str
    description: str
    typeOfTrust: Literal[
        "IRREVOC", "SMSF", "REVOCABLE", "TESTAMENTARY", "RETIREMENT", "ERISA", "OTHER"
    ]
    purposeOfTrust: str
    dateFormed: str
    formationCountry: str
    formationState: str
    registrationNumber: str
    registrationType: TINTypeEnum
    registrationCountry: str
    sameMailAddress: bool
    translated: bool


class Trust(BaseModel):
    identification: TrustIdentification
    regulatoryInformation: RegulatoryInformation


class DeleteRelationship(BaseModel):
    name: str


class UpdateEntity(BaseModel):
    addRelationships: list[AddRelationship]
    deleteRelationships: list[DeleteRelationship]
    individual: Individual
    legalEntity: LegalEntity
    trust: Trust
    organization: Organization
    documents: list[Document]
    ibEntityId: int
    externalId: str


class DeleteEntity(BaseModel):
    ibEntityId: int
    externalId: str


class InformationChange(BaseModel):
    addEntities: list[AddEntity]
    updateEntities: list[UpdateEntity]
    deleteEntities: list[DeleteEntity]
    ibAccountId: str


class OrganizationApplicant(BaseModel):
    pass


class IndividualApplicant(BaseModel):
    pass


class JointApplicant(BaseModel):
    pass


class TrustApplicant(BaseModel):
    pass


class Customer(BaseModel):
    organization: OrganizationApplicant
    accountHolder: IndividualApplicant
    jointHolders: JointApplicant
    trust: TrustApplicant
    id: str
    externalId: str
    transferUsMicroCapStock: bool
    type: CustomerTypeEnum
    prefix: str
    userName: str
    userNameAlias: str
    userNameSource: str
    email: str
    mdStatusNonPro: bool
    preferredPrimaryLanguage: str
    preferredSecondaryLanguage: str
    legalResidenceCountry: str
    taxTreatyCountry: str
    meetAmlStandard: str
    meetsAmlStandard: str
    directTradingAccess: bool
    originCountry: str
    terminationAge: int
    governingState: str
    optForDebitCard: bool
    roboFaClient: bool
    independentAccount: bool
    paperAccount: bool


class UserPrivilege(BaseModel):
    externalAccountId: str
    privilege: Literal["OWNER", "TRADER", "CUSTOM", "NONE"]


class User(BaseModel):
    userPrivileges: list[UserPrivilege]
    mdServices: list[int]
    id: str
    externalUserId: str
    externalIndividualId: str
    encryptedPassword: str
    encryptedKeyName: str
    prefix: str


class AddAdditionalAccount(BaseModel):
    customer: Customer
    account: Account
    documents: list[Document]
    users: list[User]
    accountId: str


class AllocateVAN(BaseModel):
    accountId: str
    currency: BaseCurrencyEnum
    countryCode: str


class CreateUser(BaseModel):
    accountId: str
    prefix: str
    userName: str
    id: str
    externalId: str
    authorizedTrader: bool


class UpdateTaxForm(BaseModel):
    localTaxForms: list[LocalTaxForm]
    w8Ben: FormW8BEN
    w8BenE: FormW8BENE
    w9: FormW9
    translation: bool
    inputLanguage: LanguageEnum
    accountId: str
    documents: list[Document]
    entityId: str
    externalId: str


class AnswerDetail(BaseModel):
    name: str
    detail: str


class Answer(BaseModel):
    answerDetail: list[AnswerDetail]
    detail: str
    id: int
    questionId: int


class Questionnaire(BaseModel):
    answers: list[Answer]
    formNumber: int


class QuestionnairesWithAccount(BaseModel):
    questionnaire: list[Questionnaire]
    accountId: str


class Details(BaseModel):
    question: str
    answer: str


class SecurityQuestions(BaseModel):
    details: list[Details]
    referenceUserName: str
    inputLanguage: LanguageEnum


class ApplyFeeTemplate(BaseModel):
    accountId: str
    templateName: str


class Task(BaseModel):
    formNumber: int
    status: bool


class QuizQuestionnaires(BaseModel):
    questionnaire: list[Questionnaire]
    accountId: str
    task: list[Task]


class AccountManagementRequests(BaseModel):
    updateExternalId: UpdateExternalId
    updatePropertyProfile: UpdatePropertyProfile
    updateAccountAlias: UpdateAccountAlias
    changeBaseCurrency: ChangeBaseCurrency
    abandonAccount: AbandonAccount
    addNewUser: AddNewUser
    addLevFxCapability: AddLEVFXCapability
    addMiFirData: AddMiFIRData
    addTradingPermissions: AddTradingPermissions
    removeTradingPermissions: RemoveTradingPermissions
    changeMarginType: ChangeMarginType
    addCLPCapability: AddCLPCapability
    changeFinancialInformation: ChangeFinancialInformation
    resetAbandonedAccount: ResetAbandonedAccount
    updateCredentials: list[UpdateCredentials]
    updateAccountRepresentatives: UpdateAccountRepresentatives
    completeLoginMessage: CompleteLoginMessage
    reopenAccount: ReopenAccount
    enrollInSyep: EnrollInSYEP
    leaveSyep: LeaveSYEP
    enrollInDrip: EnrollInDRIP
    leaveDrip: LeaveDRIP
    duplicateAccount: DuplicateAccount
    documentSubmission: DocumentSubmission
    processDocuments: ProcessDocuments
    updateBcan: UpdateBCAN
    prohibitedCountryQuestionnaire: ProhibitedCountryQuestionnaire
    updateWithholdingStatement: UpdateWithholdingStatement
    accreditedInvestor: AccreditedInvestor
    changeAccountHolderDetail: ChangeAccountHolderDetail
    updateUserAccessRights: UpdateUserAccessRights
    informationChange: InformationChange
    addAdditionalAccount: AddAdditionalAccount
    accountConfiguration: AccountConfiguration
    allocateVan: AllocateVAN
    createUser: CreateUser
    updateTaxForm: UpdateTaxForm
    questionnaires: QuestionnairesWithAccount
    securityQuestions: SecurityQuestions
    applyFeeTemplate: ApplyFeeTemplate
    accountClose: AccountClose
    manageMarketDataSubscriptions: list[ManageMarketDataSubscriptions]
    quizQuestionnaires: QuizQuestionnaires
