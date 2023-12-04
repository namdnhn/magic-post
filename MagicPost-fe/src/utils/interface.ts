export enum Roles {
	ADMIN = 1,
	TRANSACTION_LEADER = 2,
	TRANSACTION_STAFF = 3,
	GATHERING_LEADER = 4,
	GATHERS_STAFF = 5,
	CUSTOMER = 6,
	SHIPPER = 7
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

export interface OfficesInterface {
	id: string;
	pointId: string;
	name: string;
	phoneNo: string;
	address: string;
	admin: {
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
