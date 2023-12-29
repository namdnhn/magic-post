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

export enum OrderType {
	CUSTOMER = 1,
	GATHERING = 2,
	TRANSACTION = 3,
	DELIVERY = 4
}

export enum OrderStatus {
	NEW = 1,
	PROCESSING = 2,
	CREATE_SEND = 3,
	CONFIRM_SEND = 4,
	CONFIRM_RECEIVE = 5,
	SUCCESS_DELIVERY = 6,
	FAILED_DELIVERY = 7,
	COMPLETED = 8
}