/**
 * Created by ThinkPad on 5/8/2017.
 */
import { Component } from '@angular/core';
import { KilnService } from './kiln.service';

@Component({
  selector: 'my-app',
  template: `
    <h1>{{title}}</h1>
    <nav>
    <a routerLink="/dashboard" routerLinkActive="active">Dashboard</a>
    <a routerLink="/kilns" routerLinkActive="active">Kilns</a>
    </nav>
    <router-outlet></router-outlet>
  `,
  styleUrls: ['./app.component.css'],
  providers: [KilnService]
})

export class AppComponent {
  title = 'Kiln Manager';
}
