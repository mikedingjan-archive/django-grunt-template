module.exports = function( grunt ) {
    'use strict';

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        sass: {
            dist: {
                files: {
                    '{{ project_name }}/static/dist/main.css': '{{ project_name }}/static/sass/main.sass'
                }
            }
        },

        watch: {
            files: [
                '{{ project_name }}/static/sass/*.sass'
            ],
            tasks: [ 'sass' ]
        }

    });

    grunt.loadNpmTasks( 'grunt-contrib-sass' );
    grunt.loadNpmTasks( 'grunt-contrib-watch' );

    grunt.registerTask( 'default', ['sass'] );

};
