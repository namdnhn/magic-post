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

export interface Paginate {
	totalPages: number;
	totalItems: number;
	perPage: number;
	currentPage: number;
}

export interface LocationSchema {
	name: string;
	code: number;
}

export interface StaffsInteface {
	id: string;
	userId: string;
	address: string;
	email: string;
	fullName: string;
	phoneNo: string;
	dateOfBirth: string;
	role: {
		id: Roles;
		name: string;
	};
	workAt: {
		id: string;
		pointId: string;
		name: string;
	};
}

export interface GatherOrderInteface {
	orderId: string;
	address: string;
}

export interface OfficesInterface {
	id: string;
	pointId: string;
	name: string;
	phoneNo: string;
	address: string;
	leader: {
		fullName: string;
		userId: string;
	};
	gatheringPoint?: {
		id: string;
		pointId: string;
		name: string;
	};
	type: string;
}

export interface TransactionOrderInteface {
	orderId: string;
	address: string;
	transactionId: string;
}
