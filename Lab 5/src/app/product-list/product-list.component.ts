import { Component, Input, OnInit} from '@angular/core';
import { Product, products } from 'src/products';
import {Router, ActivatedRoute, Params} from '@angular/router';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit{
  products = products;

  constructor(private activatedRoute: ActivatedRoute) {
    
  }

  ngOnInit(){
    this.activatedRoute.queryParams.subscribe(params => this.products = products.filter(function (product){
      return product.category.id == params['categoryId']
    }));
  }

  removeProduct(productId: number){
    this.products = this.products.filter(function(product){ return product.id != productId});
  }
}
