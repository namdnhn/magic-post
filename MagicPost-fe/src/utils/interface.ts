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

export enum Catergority {
	DOCUMENT = 1,
	PACKAGE = 2
}

export enum OrderStatus {
	NEW = 1,
	PROCESSING = 2,
	CONFIRM_SEND = 3,
	CONFIRM_RECEIVE = 4,
	SUCCESS_DELIVERY = 5,
	FAILED_DELIVERY = 6
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

export interface CustomerInterface {
	user_id: number;
	email: string;
	fullname: string;
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


export interface Order {
	orderId: number;
	mainCharge: number;
	orderDelivery: {
		id: number;
		fromLocation: {
			id: string;
			customerId: number;
			name: string;
			phoneNo: string;
			address: string;
			// transactionPoint: OfficesInterface;
		};
		// currentLocation: OfficesInterface;
		toLocation: {
			id: string;
			customerId: number;
			name: string;
			phoneNo: string;
			address: string;
			// transactionPoint: OfficesInterface;
		};
		
	};
	createAt: string;
}
