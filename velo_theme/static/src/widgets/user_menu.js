odoo.define('velo_theme.UserMenu', function (require) {
"use strict";

var config = require('web.config');
var core = require('web.core');
var framework = require('web.framework');
var Dialog = require('web.Dialog');
var Widget = require('web.Widget');
var _t = core._t;
var QWeb = core.qweb;

var UserMenu = require('web.UserMenu');
// Modify behaviour of addons/web/static/src/js/widgets/user_menu.js
UserMenu.include({
    // _onMenuAbout: function () {
    //     window.open('https://www.odoo.com/documentation/user', '_blank');
    // },
    _onMenuAbout: function () {
        new Dialog(this, {
            size: 'large',
            dialogClass: 'o_act_window',
            title: _t("About"),
            $content: $(QWeb.render("UserMenu.about"))
        }).open();
    }
});
});