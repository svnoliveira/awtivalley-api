module.exports = {
  apps: [
    {
      name: 'awtiapi',
      script: 'manage.py',
      args: 'runserver 7000',
      interpreter: 'python',
      watch: true,
      env: {
        DJANGO_SETTINGS_MODULE: '_core.settings',
      },
    },
  ],
};

