"""Flask application for Task Optimization System."""

import os
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from dotenv import load_dotenv
from src.optimizer import TaskOptimizer

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
api = Api(app)

# Initialize task optimizer
optimizer = TaskOptimizer()


class OptimizeEndpoint(Resource):
    """API endpoint for task optimization."""

    def post(self):
        """Process optimization request."""
        try:
            data = request.get_json()
            tasks = data.get('tasks')
            constraints = data.get('constraints')

            # Set tasks and constraints
            optimizer.set_tasks(tasks)
            optimizer.set_constraints(constraints)

            # Run optimization
            result = optimizer.optimize()

            return {
                'status': 'success',
                'optimized_schedule': result['schedule'],
                'metrics': result['metrics']
            }, 200

        except Exception as e:
            return {'status': 'error', 'message': str(e)}, 400


class MetricsEndpoint(Resource):
    """API endpoint for performance metrics."""

    def get(self):
        """Get performance metrics."""
        try:
            metrics = optimizer.get_metrics()
            return {'status': 'success', 'metrics': metrics}, 200
        except Exception as e:
            return {'status': 'error', 'message': str(e)}, 400


class HealthCheck(Resource):
    """Health check endpoint."""

    def get(self):
        """Return application health status."""
        return {'status': 'healthy'}, 200


# Register API routes
api.add_resource(HealthCheck, '/api/health')
api.add_resource(OptimizeEndpoint, '/api/optimize')
api.add_resource(MetricsEndpoint, '/api/metrics')


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return {'status': 'error', 'message': 'Endpoint not found'}, 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return {'status': 'error', 'message': 'Internal server error'}, 500


if __name__ == '__main__':
    # Run the application
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', False)
    app.run(host='0.0.0.0', port=port, debug=debug)
