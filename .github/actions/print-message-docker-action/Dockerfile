# Use an official Node.js runtime as a parent image
FROM node:16

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the entrypoint script to the container
COPY entrypoint.sh /usr/src/app/entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x entrypoint.sh

# Set the default command to run the entrypoint script
ENTRYPOINT ["./entrypoint.sh"]
