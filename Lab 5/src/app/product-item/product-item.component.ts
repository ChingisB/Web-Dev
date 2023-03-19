import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Category } from 'src/categories';
import { Product } from 'src/products';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent {
  @Input() product: Product = new Product('', '', '', 10, '', new Category("", ""));
  @Output() removeProductEvent = new EventEmitter<number>();
  like: boolean = false;

  constructor() {
    
  }

  removeProduct(value: number){
    this.removeProductEvent.emit(value);
  }

  clickLike(){
    if(this.like){
      this.product.likes--;
    }
    else{
      this.product.likes++;
    }
    this.like = !this.like;
  }
}
