# 1. Start with a base operating system that has Java 17 installed
FROM eclipse-temurin:17-jre-alpine

# 2. creating a volume for temporary files
VOLUME /tmp

# 3. Copy the built application file (JAR) from our computer into the container
COPY target/*.jar app.jar

# 4. Open port 8080 so the outside world can talk to the app
EXPOSE 8080

# 5. The command to run when the container starts
ENTRYPOINT ["java", "-jar", "/app.jar"]