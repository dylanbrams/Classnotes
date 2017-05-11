/**
 * Created by ThinkPad on 5/8/2017.
 */
import { Component, Input, OnInit }         from '@angular/core';
import { ActivatedRoute, Params }   from '@angular/router';
import { Location }                 from '@angular/common';
import { Kiln }                     from './kiln';
import { KilnService }              from './kiln.service';
import 'rxjs/add/operator/switchMap';

@Component({
  selector: 'kiln-detail',
  templateUrl: `./kiln-detail.component.html`
})
export class KilnDetailComponent implements OnInit {
  @Input() kiln: Kiln;
  constructor(
      private kilnService: KilnService,
      private route: ActivatedRoute,
      private location: Location
  ) {}

  ngOnInit(): void {
    this.route.params
      .switchMap((params: Params) => this.kilnService.getKiln(+params['kiln_id']))
      .subscribe(kiln => this.kiln = kiln);
  }
  goBack(): void {
    this.location.back();
  }
}
