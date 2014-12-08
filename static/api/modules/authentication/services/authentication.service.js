/**Authentication
 * Authentication
 * @namespace dashboard.authentication.services
 */
(function () {
    'use strict';

    angular
        .module('dashboard.authentication.services')
        .factory('Authentication', Authentication);

    Authentication.$inject = ['$cookies', '$http'];

    /**
     * @namespace Authentication
     * @returns {Factory}
     */
    function Authentication($cookies, $http) {
        /**
         * @name Authentication
         * @desc The Factory to be returned
         */
        var Authentication = {
            getAuthenticatedAccount: getAuthenticatedAccount,
            isAuthenticated: isAuthenticated,
            authenticate: authenticate,
            logout: logout,
            setAuthenticatedAccount: setAuthenticatedAccount,
            unauthenticate: unauthenticate
        };

        return Authentication;

        /**
         * @name getAuthenticatedAccount
         * @desc Return the currently authenticated account
         * @returns {object|undefined} Account if authenticated, else `undefined`
         * @memberOf dashboard.authentication.services.Authentication
         */
        function getAuthenticatedAccount() {
            if (!$cookies.authenticatedAccount) {
                return;
            }

            return JSON.parse($cookies.authenticatedAccount);
        }

        /**
         * @name isAuthenticated
         * @desc Check if the current user is authenticated
         * @returns {boolean} True is user is authenticated, else false.
         * @memberOf dashboard.authentication.services.Authentication
         */
        function isAuthenticated() {
            return !!$cookies.authenticatedAccount;
        }


        /**
         * @name setAuthenticatedAccount
         * @desc Stringify the account object and store it in a cookie
         * @param {Object} user The account object to be stored
         * @returns {undefined}
         * @memberOf dashboard.authentication.services.Authentication
         */
        function setAuthenticatedAccount(account) {
            $cookies.authenticatedAccount = JSON.stringify(account);
        }

        /**
         * @name unauthenticate
         * @desc Delete the cookie where the user object is stored
         * @returns {undefined}
         * @memberOf dashboard.authentication.services.Authentication
         */
        function unauthenticate() {
            delete $cookies.authenticatedAccount;
        }

        /**
         * @name authenticate
         * @returns {Promise}loginErrorFn
         * @memberOf dashboard.authentication.services.Authentication
         */
        function authenticate() {
            return $http.get('/users/detail').then(loginSuccessFn, loginErrorFn);

            /**
             * @name loginSuccessFn
             * @desc Set the authenticated account and redirect to index
             */
            function loginSuccessFn(data, status, headers, config) {
                Authentication.setAuthenticatedAccount(data.data);
            }

            /**
             * @name loginErrorFn
             * @desc Log "Epic failure!" to the console
             */
            function loginErrorFn(data, status, headers, config) {
                /*window.location = '/accounts/login/'*/
                console.log('ERROR - GET USER DETAL');
            }
        }

        /**
         * @name logout
         * @desc Try to log the user out
         * @returns {Promise}
         * @memberOf dashboard.authentication.services.Authentication
         */
        function logout() {
            return $http.post('/users/logout/')
                .then(logoutSuccessFn, logoutErrorFn);

            /**
             * @name logoutSuccessFn
             * @desc Unauthenticate and redirect to index with page reload
             */
            function logoutSuccessFn(data, status, headers, config) {
                Authentication.unauthenticate();

                window.location = '/';
            }

            /**
             * @name logoutErrorFn
             * @desc Log "Epic failure!" to the console
             */
            function logoutErrorFn(data, status, headers, config) {
                console.error('Epic failure!');
            }
        }


    }
})();