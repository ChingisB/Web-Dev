import { Component } from '@angular/core';
import { Category, categories } from 'src/categories';
import { products } from 'src/products';

@Component({
  selector: 'app-category-list',
  templateUrl: './category-list.component.html',
  styleUrls: ['./category-list.component.css']
})
export class CategoryListComponent {
  categories = categories;
  products = products;

  getProductsByCategory(category:Category) {
    return products.filter(function(obj) { return obj.category == category})
  }
}
