from django.dispatch import receiver
from .signals import workflow_changed
from .selinonconfig import AutomationConfig
import json



@receiver(workflow_changed, dispatch_uid="automation_workflow_changed")
def receive_workflow_change(sender, workflowSpec, **kwargs):
	config = AutomationConfig(sender)
	sender.flowspec = json.dumps(config.construct_flow_definition())
	sender.save()
