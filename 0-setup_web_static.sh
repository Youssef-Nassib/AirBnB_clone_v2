nstall Nginx if it is not already installed
if ! nginx -v > /dev/null 2>&1; then
	    sudo apt update
	        sudo apt install -y nginx
fi

# Create the required directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "<html>
  <head>
    </head>
      <body>
          Holberton School
	    </body>
	    </html>" | sudo tee /data/web_static/releases/test/index.html

	    # Create a symbolic link, and remove existing one if it exists
	    if [ -L /data/web_static/current ]; then
		        sudo rm /data/web_static/current
	    fi
	    sudo ln -s /data/web_static/releases/test/ /data/web_static/current

	    # Give ownership of the /data/ folder to the ubuntu user and group
	    sudo chown -R ubuntu:ubuntu /data/

	    # Update the Nginx configuration
	    nginx_conf="/etc/nginx/sites-available/default"
	    if ! grep -q "location /hbnb_static" $nginx_conf; then
		        sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' $nginx_conf
	    fi

	    # Restart Nginx
	    sudo service nginx restart

	    # Ensure the script exits successfully
	    exit 0
