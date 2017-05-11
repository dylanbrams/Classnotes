/**
 * Created by ThinkPad on 5/8/2017.
 */
import { Component, OnInit } from '@angular/core';
import { Kiln } from './kiln';
import { KilnService } from './kiln.service';

@Component({
  selector: 'my-dashboard',
  templateUrl: `./dashboard.component.html`,
  styleUrls: [ './dashboard.component.css' ]

})
export class DashboardComponent implements OnInit {
  kilns: Object[] = [];
  constructor(private kilnService: KilnService) {}
  ngOnInit(): void {
    this.kilnService.getKilns().then(kilns => this.kilns = kilns);
  }
}
