(function () {
    'use strict';

    angular
        .module('dashboard', [
            'dashboard.config',
            'dashboard.routes',
            'dashboard.authentication',
            'dashboard.profile'
        ]);

    angular
        .module('dashboard.routes', ['ngRoute']);

    angular
        .module('dashboard.config', []);



    angular
        .module('dashboard')
        .run(run);

    run.$inject = ['$http', 'Authentication'];

    /**
     * @name run
     * @desc Update xsrf $http headers to align with Django's defaults
     */
    function run($http, Authentication) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';

        Authentication.authenticate();
    }
})();