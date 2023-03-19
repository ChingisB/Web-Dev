import { Category, gamepads, headphones, phones, tv } from "./categories";
import { IDescriptive } from "./descriptive";

export class Product implements IDescriptive{
    static idCount: number = 0;
    id: number = 0;
    image: string = "";
    name: string = "";
    description: string = " ";
    rating: number = 0;
    link: string = "";
    category: Category = new Category('', '');
    likes: number = 0;

    constructor(image: string, name: string, description: string, rating: number, link: string, category: Category){
      this.id = ++Product.idCount;
      this.image = image;
      this.name = name;
      this.description = description;
      this.rating = rating
      this.link = link;
      this.category = category;
    }
}
  
export const products = [
    new Product('iphone.jpg', 'Apple Iphone 13', 'Apple iPhone 13 received a 6.1-inch Super something', 
    4.5, 'https://kaspi.kz/shop/p/apple-iphone-13-128gb-chernyi-102298404/?c=750000000#!/item', phones),


    new Product('xiaomi.jpg', 'Xiaomi Redmi Note 10 Pro', 'The screen refresh rate is 120 Hz. Screen type color AMOLED, touch',
    4.8, 'https://kaspi.kz/shop/p/xiaomi-redmi-note-10-pro-8-gb-256-gb-seryi-107221005/?c=750000000#!/item', phones),


    new Product( 'samsung.jpg', 'Samsung Galaxy A23', 'Discover more possibilities. Get everything at once. 6.6-inch TFT display Galaxy A23',
    4.3, 'https://kaspi.kz/shop/p/samsung-galaxy-a23-6-gb-128-gb-chernyi-104348541/?c=750000000#!/item', phones),


    new Product('one_plus.jpg', 'OnePlus 10 Pro', 'Integrated metal frame with 3D nano-microcrystalline ceramics',
    3.3, 'https://kaspi.kz/shop/p/oneplus-10-pro-12-gb-256-gb-chernyi-global-version-104314136/?c=750000000#!/item', phones),


    new Product('vivo.jpg', 'Vivo Y35', 'Screen refresh rate 90 Hz Screen Type LCD IPS',
    2.9, 'https://kaspi.kz/shop/p/vivo-y35-4-gb-128-gb-zolotistyi-107358117/?c=750000000#!/item', phones),


    new Product('google_pixel.jpg', 'Google Pixel 6a', 'Screen Type Super AMOLED, Capacitive, Multitouch Diagonal6.2 inches',
    3.9, 'https://kaspi.kz/shop/p/google-pixel-6a-6-gb-128-gb-chernyi-106250318/?c=750000000#!/item', phones),


    new Product('airpods.jpg', 'Apple AirPods', 'AirPods are configured in one touch. Automatically turn on and establish a connection.', 
    4.9, 'https://kaspi.kz/shop/p/apple-airpods-with-charging-case-belyi-4804056/?c=750000000#!/item', headphones),


    new Product('airpods3.jpg', 'Apple AirPods 3', 'The dynamic driver developed by Apple uses a special amplifier, providing incredible sound detail.',
    3.8, 'https://kaspi.kz/shop/p/apple-airpods-3-belyi-102667744/?c=750000000#!/item', headphones),


    new Product('buds.jpg', 'Samsung Galaxy Buds 2', 'Discover your own world with Galaxy Buds2. Advanced two-way acoustics', 
    5.0, 'https://kaspi.kz/shop/p/samsung-galaxy-buds-2-sm-r177nzkacis-chernyi-102046373/?c=750000000#!/item', headphones),


    new Product('marshall.jpg', 'Marshall Major IV', 'The MARSHALL Major IV Bluetooth headset, thanks to its features, will give you a comfortable listening to music', 
    4.9, 'https://kaspi.kz/shop/p/marshall-major-iv-chernyi-102138144/?c=750000000#!/item', headphones),

    new Product('tws.jpg', 'TWS F9-5', 'TWS 9-5 Wireless Bluetooth headphones They are very practical, completely wireless and do not need a cable', 
    1, 'https://kaspi.kz/shop/p/tws-f9-5-chernye-101769530/?c=750000000#!/item', headphones),
  
    new Product('dualsence.jpg', 'PS5 DualSense', 'The PlayStation DualSense 5 gamepad provides full control over the gameplay and immersion in the world of virtual reality.', 
    4.9, 'https://kaspi.kz/shop/p/sony-ps5-dualsense-belyi-100752003/?c=750000000#!/item', gamepads),

    new Product('dualshock.jpg', 'Sony Dualshock 4', 'The new DUALSHOCK 4 wireless controller for Playstation 4.', 
    4.7, 'https://kaspi.kz/shop/p/sony-dualshock-4-v2-chernyi-13000002/?c=750000000#!/item', gamepads),

    new Product('xbox.jpg', 'Microsoft Xbox QAS', 'Xbox Wireless Gamepad: Triggers and bumpers with textured surface', 
    3.9, 'https://kaspi.kz/shop/p/microsoft-xbox-qas-00002-belyi-100780577/?c=750000000#!/item', gamepads),

    new Product('pubg.jpg', 'PUBG Corporation SR', 'This gamepad is suitable for Android and IOS smartphones with dimensions up to 16 cm wide and up to 9 cm high', 
    2, 'https://kaspi.kz/shop/p/pubg-corporation-sr-2000-chernyi-102100408/?c=750000000#!/item', gamepads),

    new Product('njos.jpg', 'Artifact NJOS', 'Our Artificial NJOS M3 gaming gamepad for smartphones will take your game to a new level!', 
    3.2, 'https://kaspi.kz/shop/p/artifact-njos-m3-chernyi-103347636/?c=750000000#!/item', gamepads),

    new Product('yasin.jpg', 'Yasin LED-32E7000', 'Thanks to the HD resolution, the viewer will be happy to watch any movie on his TV, because his image will be beyond praise.',
    5.0, 'https://kaspi.kz/shop/p/yasin-led-32e7000-81-sm-chernyi-103411518/?c=750000000#!/item', tv),

    new Product('samsung_tv.jpg', 'Samsung UE43T5300AUXCE', 'Watch HD content with improved clarity and the most accurate color reproduction.',
    4.0, 'https://kaspi.kz/shop/p/samsung-ue43t5300auxce-109-sm-chernyi-100182013/?c=750000000#!/item', tv),

    new Product('xiaomi.jpg', 'Xiaomi TV P1', 'The innovative design of Xiaomi TV P1 32 without a frame on three sides provides a higher screen-to-body ratio, a clear image',
    3.0, 'https://kaspi.kz/shop/p/xiaomi-tv-p1-32-l32m6-6arg-81-sm-chernyi-103039169/?c=750000000#!/item', tv),

    new Product('lg.jpg', 'LG 43LM5772PLA', 'LG HD TVs allow you to enjoy a higher-quality image thanks to high resolution and bright colors.',
    2.0, 'https://kaspi.kz/shop/p/lg-43lm5772pla-109-sm-chernyi-101293496/?c=750000000#!/item', tv),

    new Product('tcl.jpg', 'TCL 43P615', 'TV TCL 43P615 – 4K HDR model based on Android with surround sound and rich color reproduction.',
    1.0, 'https://kaspi.kz/shop/p/tcl-43p615-109-sm-chernyi-102569498/?c=750000000#!/item', tv),
    
];
  