"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var core_1 = require("@angular/core");
var KILNS = [
    { id: 11, name: 'Dylan\'s First Kiln' }
];
var AppComponent = (function () {
    function AppComponent() {
        this.title = 'Kiln Management List';
        this.kilns = KILNS;
    }
    AppComponent.prototype.onSelectKiln = function (kiln) {
        this.selectedKiln = kiln;
    };
    return AppComponent;
}());
AppComponent = __decorate([
    core_1.Component({
        selector: 'my-app',
        template: "    \n    <h1>{{title}}</h1>\n    <h2>My Kilns</h2>\n    <ul class=\"kilns\">\n      <li *ngFor=\"let current_kiln of kilns\"\n        [class.selected]=\"current_kiln === selectedKiln\"\n        (click)=\"onSelect(selectedKiln)\">\n        <span class=\"badge\">{{current_kiln.id}}</span> {{current_kiln.name}}\n      </li>\n    </ul>\n    <kiln-detail [kiln]=\"current_kiln\"></kiln-detail>\n    \n  ",
        styles: ["\n    .selected {\n      background-color: #CFD8DC !important;\n      color: white;\n    }\n    .kilns {\n      margin: 0 0 2em 0;\n      list-style-type: none;\n      padding: 0;\n      width: 15em;\n    }\n    .kilns li {\n      cursor: pointer;\n      position: relative;\n      left: 0;\n      background-color: #EEE;\n      margin: .5em;\n      padding: .3em 0;\n      height: 1.6em;\n      border-radius: 4px;\n    }\n    .kilns li.selected:hover {\n      background-color: #BBD8DC !important;\n      color: white;\n    }\n    .kilns li:hover {\n      color: #607D8B;\n      background-color: #DDD;\n      left: .1em;\n    }\n    .kilns .text {\n      position: relative;\n      top: -3px;\n    }\n    .kilns .badge {\n      display: inline-block;\n      font-size: small;\n      color: white;\n      padding: 0.8em 0.7em 0 0.7em;\n      background-color: #607D8B;\n      line-height: 1em;\n      position: relative;\n      left: -1px;\n      top: -4px;\n      height: 1.8em;\n      margin-right: .8em;\n      border-radius: 4px 0 0 4px;\n    }\n  "]
    })
], AppComponent);
exports.AppComponent = AppComponent;
//# sourceMappingURL=app.component.js.map