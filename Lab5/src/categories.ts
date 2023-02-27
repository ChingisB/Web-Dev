import { IDescriptive } from "./descriptive";

export class Category implements IDescriptive{
    static idCount = 0;
    id: number = 0;
    name: string = "";
    description: string = "";

    constructor(name: string, description: string){
        this.name = name;
        this.description = description;
        this.id = ++Category.idCount;
    }

}

export const phones: Category = new Category("Phone", "Smartphones for everyday user");
export const headphones: Category = new Category("Headphones", "Wireless stuff");
export const gamepads: Category = new Category("Gamepads", "Controllers for gamers");
export const tv: Category = new Category("Tv", "Big plasmas");


export const categories = [phones, headphones, gamepads, tv];