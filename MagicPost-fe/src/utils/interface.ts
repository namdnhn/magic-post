export enum Roles {
	ADMIN = 1,
	TRANSACTION_LEADER = 2,
	TRANSACTION_STAFF = 3,
	GATHERING_LEADER = 4,
	GATHERS_STAFF = 5,
	CUSTOMER = 6,
	SHIPPER = 7
}

export enum LocationDepth {
	PROVINCE = 1,
	DISTRICT = 2,
	WARDS = 3
}

export interface LocationSchema {
	name: string;
	code: number;
}

export interface StaffTableInteface {
	id: string;
	fullName: string;
	role: {
		id: string;
		name: string;
	};
	workAt: string;
}

export interface OfficeTableInterface {
	id: string;
	name: string;
	phone: string;
	address: string;
	manager: string;
	gatheringPoint?: string;
}

export interface TableTransactionOrderInteface {
	orderId: string;
	address: string;
	transactionId: string;
}
