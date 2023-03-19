import { Component } from '@angular/core';
import { Category, categories } from 'src/categories';
import { products } from 'src/products';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Lab4';
  categories = categories;
  products = products;

 
}
