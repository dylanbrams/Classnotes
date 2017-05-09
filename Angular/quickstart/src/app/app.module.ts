import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';

import { AppRoutingModule }  from './app-routing.module';
import { AppComponent } from './app.component';
import { KilnsComponent }  from './kilns.component';
import { KilnDetailComponent } from './kiln-detail.component';
import { KilnService } from './kiln.service';
import { DashboardComponent } from './dashboard.component';
import {HttpModule} from '@angular/http';


@NgModule({
  imports:      [ BrowserModule, FormsModule, AppRoutingModule, HttpModule],
  declarations: [ AppComponent, KilnsComponent, KilnDetailComponent, DashboardComponent ],
  providers:    [ KilnService ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
