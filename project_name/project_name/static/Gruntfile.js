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

        cssmin: {
            options: {
                banner: '/*! <%= pkg.name %> v<%= pkg.version %> <%= grunt.template.today("dd-mm-yyyy") %> */\n'
            },
            compress: {
                files: {
                    '{{ project_name }}/static/dist/{{ project_name }}.min.css': ['{{ project_name }}/static/dist/main.css']
                }
            }
        },

        concat: {
            options: {},
            dist: {
                src: [
                    '{{ project_name }}/static/src/main.js'
                ],
                dest: '{{ project_name }}/static/dist/main.js'
            }
        },

        uglify: {
            options: {
                banner: '/*! <%= pkg.name %> v<%= pkg.version %> <%= grunt.template.today("dd-mm-yyyy") %> */\n',
                report: 'gzip'
            },
            dist: {
                files: {
                    '{{ project_name }}/static/dist/{{ project_name }}.min.js': '<%= concat.dist.dest %>',
                    '{{ project_name }}/static/dist/modernizr.min.js': '{{ project_name }}/static/src/vendor/modernizr.js'
                }
            }
        },

        clean: [
            '{{ project_name }}/static/sass/',
            '{{ project_name }}/static/src',
            '{{ project_name }}/static/dist/main.css',
            '<%= concat.dist.dest %>'
        ],

        watch: {
            files: [
                '{{ project_name }}/static/sass/**/*.sass',
                '{{ project_name }}/static/src/**/*.js'
            ],
            tasks: [ 'sass', 'concat' ]
        }

    });

    grunt.loadNpmTasks( 'grunt-contrib-sass' );
    grunt.loadNpmTasks( 'grunt-contrib-watch' );
    grunt.loadNpmTasks( 'grunt-contrib-clean' );
    grunt.loadNpmTasks( 'grunt-contrib-concat' );
    grunt.loadNpmTasks( 'grunt-contrib-cssmin' );
    grunt.loadNpmTasks( 'grunt-contrib-uglify' );

    grunt.registerTask( 'default', ['sass', 'cssmin', 'concat', 'uglify'] );
    grunt.registerTask( 'production', ['sass', 'cssmin', 'concat', 'uglify', 'clean'] );

};
