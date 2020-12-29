"""
Playbook for Mal_1 offense triage
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'decision_1' block
    decision_1(container=container)

    return

def send_email_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('send_email_1() called')

    # collect data for 'send_email_1' call

    parameters = []
    
    # build parameters list for 'send_email_1' call
    parameters.append({
        'cc': "",
        'to': "adam.hulcoop@sunlife.com",
        'bcc': "",
        'body': "Flow arrived at Mal_1_Triage playbook with no valid Mal_1_  use case in container:name",
        'from': "noreply@phantom.sunlifecorp.com",
        'headers': "",
        'subject': "ERROR: Mal_1_Triage exception",
        'attachments': "",
    })

    phantom.act(action="send email", parameters=parameters, assets=['smtp'], name="send_email_1")

    return

def playbook_Phantom_PROD_5_MAL_1_Pre_Triage_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_Phantom_PROD_5_MAL_1_Pre_Triage_2() called')
    
    # call playbook "Phantom/PROD_5_MAL_1_Pre_Triage", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="Phantom/PROD_5_MAL_1_Pre_Triage", container=container)

    return

def playbook_Phantom_HELPER_NullPlaybook_1_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_Phantom_HELPER_NullPlaybook_1_1() called')
    
    # call playbook "Phantom/HELPER_NullPlaybook", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="Phantom/HELPER_NullPlaybook", container=container)

    return

def playbook_Phantom_HELPER_NullPlaybook_2_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_Phantom_HELPER_NullPlaybook_2_2() called')
    
    # call playbook "Phantom/HELPER_NullPlaybook", returns the playbook_run_id
    playbook_run_id = phantom.playbook(playbook="Phantom/HELPER_NullPlaybook", container=container)

    return

def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_1() called')
    
    name_value = container.get('name', None)
    name_value = container.get('name', None)
    name_value = container.get('name', None)

    # check for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["Mal_1_Pre", "in", name_value[:18]],
        ])

    # call connected blocks if condition 1 matched
    if matched_artifacts_1 or matched_results_1:
        playbook_Phantom_PROD_5_MAL_1_Pre_Triage_2(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'elif' condition 2
    matched_artifacts_2, matched_results_2 = phantom.condition(
        container=container,
        conditions=[
            ["Mal_1_Post", "in", name_value[:18]],
        ])

    # call connected blocks if condition 2 matched
    if matched_artifacts_2 or matched_results_2:
        playbook_Phantom_HELPER_NullPlaybook_2_2(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'elif' condition 3
    matched_artifacts_3, matched_results_3 = phantom.condition(
        container=container,
        conditions=[
            ["Mal_1_Unk", "in", name_value[:18]],
        ])

    # call connected blocks if condition 3 matched
    if matched_artifacts_3 or matched_results_3:
        playbook_Phantom_HELPER_NullPlaybook_1_1(action=action, success=success, container=container, results=results, handle=handle)
        return

    # call connected blocks for 'else' condition 4
    send_email_1(action=action, success=success, container=container, results=results, handle=handle)

    return

def on_finish(container, summary):
    phantom.debug('on_finish() called')
    # This function is called after all actions are completed.
    # summary of all the action and/or all details of actions
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    return