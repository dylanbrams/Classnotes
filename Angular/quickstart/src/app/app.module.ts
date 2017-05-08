import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';

import { AppComponent }  from './app.component';
import { KilnDetailComponent } from './kiln-detail.component';

@NgModule({
  imports:      [ BrowserModule, FormsModule ],
  declarations: [ AppComponent, KilnDetailComponent ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
