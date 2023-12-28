export enum Roles {
	ADMIN = "admin",
    TRANSACTION_LEADER = "transaction_leader",
    TRANSACTION_STAFF = "transaction_staff",
    GATHERING_LEADER = "gathering_leader",
    GATHERS_STAFF = "gathering_staff",
    CUSTOMER = "customer",
    SHIPPER = "shipper"
}

export enum OfficeType {
	GATHERING = 'GP',
	TRANSACTION = 'TP'
}

export enum LocationDepth {
	PROVINCE = 1,
	DISTRICT = 2,
	WARDS = 3
}