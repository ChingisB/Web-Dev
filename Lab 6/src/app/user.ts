export interface User {
    id: number;
    name: string;
    username: string;
    email: string;
    address: object;
    phone: string;
    website: string;
    company: object;
}


export class User implements User{
    constructor(data: User){
        this.id = data.id;
        this.name = data.name;
        this.username = data.username;
        this.email = data.email;
        this.address = data.address;
        this.phone = data.phone;
        this.website = data.website;
        this.company = data.company;
    }
}
