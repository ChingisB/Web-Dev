import { Component } from '@angular/core';
import { products } from 'src/products';


@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent {
  products = products;

  show(){
    alert(products);
  }
  
}