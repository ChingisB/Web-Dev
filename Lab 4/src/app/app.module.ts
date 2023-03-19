import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ProductsComponent } from './products/products.component';
import { TopBarComponent } from './top-bar/top-bar.component';
import { RouterModule } from '@angular/router';
import { ProductDetailsComponent } from './product-details/product-details.component';

@NgModule({
  declarations: [
    AppComponent,
    ProductsComponent,
    TopBarComponent,
    ProductDetailsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule.forRoot([
      { path: '', component: ProductsComponent },
    ]),
  ],
  providers: [],
  bootstrap: [AppComponent],
  
})
export class AppModule { }
