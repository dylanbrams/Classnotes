"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
/**
 * Created by ThinkPad on 5/8/2017.
 */
var core_1 = require("@angular/core");
var kiln_service_1 = require("./kiln.service");
var AppComponent = (function () {
    function AppComponent() {
        this.title = 'Kiln Manager';
    }
    return AppComponent;
}());
AppComponent = __decorate([
    core_1.Component({
        selector: 'my-app',
        template: "\n    <h1>{{title}}</h1>\n    <nav>\n    <a routerLink=\"/dashboard\" routerLinkActive=\"active\">Dashboard</a>\n    <a routerLink=\"/kilns\" routerLinkActive=\"active\">Kilns</a>\n    </nav>\n    <router-outlet></router-outlet>\n  ",
        styleUrls: ['./app.component.css'],
        providers: [kiln_service_1.KilnService]
    })
], AppComponent);
exports.AppComponent = AppComponent;
//# sourceMappingURL=app.component.js.map