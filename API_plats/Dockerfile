# Utilisation de l'image officielle PHP avec Apache pour Laravel
FROM php:8.2-apache

# Mise à jour et installation des dépendances
RUN apt update && apt install -y \
    libpng-dev \
    libjpeg-dev \
    nodejs \
    npm \
    libfreetype6-dev \
    zip \
    unzip \
    git \
    && docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install -j$(nproc) gd pdo pdo_mysql

# Activer les modules Apache nécessaires pour Laravel
RUN a2enmod rewrite headers

# Définition du répertoire de travail dans le conteneur
WORKDIR /var/www/html

# Copie des fichiers de l'application Laravel dans le répertoire de travail
COPY . /var/www/html/
RUN cd /var/www/html
RUN cp -n .env.example .env

# Installation des dépendances PHP avec Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && cd /var/www/html/ \
    && composer install --no-dev --optimize-autoloader

# Configuration du propriétaire des fichiers pour Apache
RUN chown -R www-data:www-data /var/www/html \
    && chmod -R 755 /var/www/html

# Configuration d'Apache pour utiliser le dossier public comme DocumentRoot
RUN sed -i 's/DocumentRoot \/var\/www\/html/DocumentRoot \/var\/www\/html\/public/g' /etc/apache2/sites-available/000-default.conf

# Generate security key
RUN php artisan key:generate
# Optimizing Configuration loading
RUN php artisan config:cache
# Optimizing Route loading
RUN php artisan route:cache
# Optimizing View loading
RUN php artisan view:cache
RUN php artisan migrate --pretend --force

# Compilation des assets de Breeze (ou de votre site)
RUN npm install
RUN npm run build

# Exposition du port 80 pour Apache
EXPOSE 80
# Exposition du port 80 pour l'application
EXPOSE 8000

# Commande pour démarrer Apache
CMD ["apache2-foreground"]