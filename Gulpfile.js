var gulp = require('gulp'),
    minifyCSS = require('gulp-minify-css'),
    concatCss = require('gulp-concat-css'),
    concatJs = require('gulp-concat'),
    notify = require('gulp-notify'),
    uglify = require('gulp-uglify');

gulp.task('js-dashboard-app', function()
{

    var js_array = [
        'static/dashboard/app.js',
        'static/dashboard/app.config.js',
        'static/dashboard/app.routes.js',
        'static/dashboard/layout/layout.module.js',
        'static/dashboard/layout/controllers/layout.controller.js',
        'static/dashboard/layout/controllers/sidebar.controller.js',
        'static/dashboard/layout/controllers/nav.controller.js',
        'static/dashboard/utils/util.module.js',
        'static/dashboard/utils/directives/google-places.directive.js',
        'static/dashboard/utils/directives/really-click.directive.js',
        'static/dashboard/utils/directives/alert-notification.directive.js',
        'static/dashboard/utils/directives/upload-file-model.directive.js',
        'static/dashboard/utils/directives/upload-file-client.directive.js',
        'static/dashboard/utils/directives/upload-multiple-image.directive.js',
        'static/dashboard/utils/controllers/upload-multiple-images.controller.js',
        'static/dashboard/profile/profile.module.js',
        'static/dashboard/profile/services/profile.service.js',
        'static/dashboard/profile/controllers/detail-profile.controller.js',
        'static/dashboard/profile/controllers/update-profile.controller.js',
        'static/dashboard/profile/controllers/change-password.controller.js',
        'static/dashboard/profile/controllers/update-address.controller.js',
        'static/dashboard/item/item.module.js',
        'static/dashboard/item/services/item.service.js',
        'static/dashboard/item/controllers/item.controller.js',
        'static/dashboard/item/controllers/item-create.controller.js',
        'static/dashboard/item/controllers/item-update.controller.js',
        'static/dashboard/message/message.module.js',
        'static/dashboard/message/services/message.service.js',
        'static/dashboard/message/controllers/message.controller.js',
        'static/dashboard/message/controllers/messageThread.controller.js',
        'static/dashboard/user-location/location.module.js',
        'static/dashboard/user-location/services/location.service.js',
        'static/dashboard/user-location/controllers/location.controller.js',
        'static/dashboard/favorite/favorite.module.js',
        'static/dashboard/favorite/services/favorite.service.js',
        'static/dashboard/favorite/controllers/favorite.controller.js',
        'static/dashboard/notification/notification.module.js',
        'static/dashboard/notification/services/notification.service.js',
        'static/dashboard/notification/controllers/config-notification.controller.js',
        'static/dashboard/store/store.module.js',
        'static/dashboard/store/services/store.service.js',
        'static/dashboard/store/controllers/config-store.controller.js'
    ];

    //'static/dashboard/*.js',
    //'static/dashboard/**/*.js'
    gulp.src(js_array)
        .pipe(concatJs('concat-app.js'))
        .pipe(uglify())
        .pipe(gulp.dest('static/production/dashboard'))
        .pipe(notify("Ha finalizado la tarea de minificar y concatenar los archivos de dashboard js!"));
});

gulp.task('js-dashboard-lib', function(){

    var js_array = [
        'static/bower_components/pace-master/pace.js',
        'static/bower_components/jquery-slimscroll/jquery.slimscroll.js',
        'static/bower_components/bootstrap/dist/js/bootstrap.js',
        'static/js/theme/theme.js',
        'static/bower_components/leaflet/dist/leaflet.js',
        'static/bower_components/ng-ckeditor/libs/ckeditor/ckeditor.js',
        'static/bower_components/bootstrap-datepicker/js/bootstrap-datepicker.js',
        'static/bower_components/angular/angular.js',
        'static/bower_components/angular-route/angular-route.js',
        'static/bower_components/angular-ui-router/release/angular-ui-router.js',
        'static/bower_components/angular-leaflet/dist/angular-leaflet-directive.js',
        'static/bower_components/nsPopover/src/nsPopover.js',
        'static/bower_components/tg-angular-validator/dist/angular-validator.js',
        'static/bower_components/ng-table/dist/ng-table.js',
        'static/bower_components/angular-snackbar/angular.snackbar.js',
        'static/bower_components/ngDialog/js/ngDialog.js',
        'static/bower_components/angular-busy/dist/angular-busy.js',
        'static/bower_components/ng-ckeditor/ng-ckeditor.js',
        'static/bower_components/ng-currency/dist/ng-currency.js',
        'static/bower_components/angular-tooltip-master/src/tooltip.js',
        'static/bower_components/angularjs-socialshare/src/js/angular-socialshare.js'
    ];

    gulp.src(js_array)
        .pipe(concatJs('concat-lib.js'))
        .pipe(uglify())
        .pipe(gulp.dest('static/production/dashboard'))
        .pipe(notify("Ha finalizado la tarea de minificar y concatenar los archivos de dashboard js!"));
});

gulp.task('css-dashboard', function ()
{
    var css_array = [
        'static/bower_components/pace-master/themes/blue/pace-theme-flash.css',
        'static/bower_components/bootstrap/dist/css/bootstrap.css',
        'static/bower_components/leaflet/dist/leaflet.css',
        'static/css/theme/theme.css',
        'static/bower_components/bootstrap-datepicker/css/datepicker3.css',
        'static/bower_components/ngDialog/css/ngDialog.css',
        'static/bower_components/ngDialog/css/ngDialog-theme-plain.css',
        'static/bower_components/angular-snackbar/css/angular.snackbar.css',
        'static/bower_components/angular-busy/dist/angular-busy.css',
        'static/bower_components/ng-table/dist/ng-table.css',
        'static/bower_components/nsPopover/less/ns-popover.css',
        'static/bower_components/angular-tooltip-master/src/tooltip.css',
        'static/css/less/dashboard.css'
    ];
    gulp.src(css_array)
        .pipe(concatCss("concat.css"))
        .pipe(minifyCSS({keepBreaks:false}))
        .pipe(gulp.dest('static/production/dashboard'))
        .pipe(notify("Ha finalizado la tarea de minificar y concatenar los archivos dashboard css!"));
});



gulp.task('js-search', function(){

    var js_array = [
        'static/bower_components/leaflet/dist/leaflet.js',
        'static/bower_components/Leaflet.awesome-markers/dist/leaflet.awesome-markers.js',
        'static/bower_components/angular/angular.js',
        'static/bower_components/angular-leaflet/dist/angular-leaflet-directive.js',
        'static/bower_components/angular-tooltip-master/src/tooltip.js',
        'static/bower_components/angular-snackbar/angular.snackbar.min.js',

        'static/angular-resources/modules/utils/util.module.js',
        'static/angular-resources/modules/utils/directives/google-places.directive.js',
        'static/angular-resources/modules/utils/directives/ng-enter.directive.js',
        'static/angular-resources/modules/utils/directives/alert-notification.directive.js',

        'static/angular-resources/modules/item/item.module.js',
        'static/angular-resources/modules/item/services/item.service.js',
        'static/angular-resources/modules/item/controllers/item.controller.js',

        'static/angular-resources/apps/app.search.js',
        'static/angular-resources/apps/app-search.config.js'

    ];

    gulp.src(js_array)
        .pipe(concatJs('concat.js'))
        .pipe(uglify())
        .pipe(gulp.dest('static/production/search'))
        .pipe(notify("Ha finalizado la tarea de minificar y concatenar los archivos de search js!"));
});

gulp.task('css-search', function ()
{
    var css_array = [
        'static/css/less/list-item.css',
        'static/bower_components/leaflet/dist/leaflet.css',
        'static/bower_components/Leaflet.awesome-markers/dist/leaflet.awesome-markers.css',
        'static/bower_components/angular-tooltip-master/src/tooltip.css',
        'static/bower_components/angular-snackbar/css/angular.snackbar.css'
    ];
    gulp.src(css_array)
        .pipe(concatCss("concat.css"))
        .pipe(minifyCSS({keepBreaks:false}))
        .pipe(gulp.dest('static/production/search'))
        .pipe(notify("Ha finalizado la tarea de minificar y concatenar los archivos search css!"));
});