#!/usr/bin/env python3
"""
Auto-generate equipment RST pages from equipment.json
"""
import json
import os
import re

# Category mapping
CATEGORY_TO_DIR = {
    'drone': 'aerial',
    'robot': 'ground', 
    'underwater': 'water',
    'scanner': 'sensors',
    'sensor': 'sensors',
    'compute': 'sensors',  # Computing equipment goes in sensors for now
    'misc': 'sensors',      # Misc equipment goes in sensors
    'power': 'sensors'
}

def clean_filename(name):
    """Convert equipment name to valid filename"""
    filename = name.lower()
    filename = re.sub(r'[^\w\s-]', '', filename)
    filename = re.sub(r'[-\s]+', '-', filename).strip('-')
    return filename[:60]  # Limit length

def format_value(value):
    """Format a value for RST output"""
    if isinstance(value, list):
        return ', '.join(str(v) for v in value)
    elif isinstance(value, bool):
        return 'Yes' if value else 'No'
    elif value is None:
        return 'N/A'
    return str(value)

def generate_rst_content(item):
    """Generate RST content for an equipment item"""
    name = item['name']
    underline = '=' * len(name)
    
    lines = [
        underline,
        name,
        underline,
        '',
        '.. admonition:: Quick Info',
        '   :class: equipment-info',
        ''
    ]
    
    # Add quick info fields
    if item.get('manufacturer'):
        lines.append(f"   - **Manufacturer:** {item['manufacturer']}")
    if item.get('model'):
        lines.append(f"   - **Model:** {item['model']}")
    if item.get('item_class'):
        lines.append(f"   - **Category:** {item['item_class']}")
    if item.get('location'):
        lines.append(f"   - **Location:** {item['location']}")
    if item.get('primary_contact'):
        lines.append(f"   - **Contact:** {item['primary_contact']}")
    if item.get('asset_tag'):
        lines.append(f"   - **Asset Tag:** {item['asset_tag']}")
    
    lines.extend(['', 'Overview', '--------', ''])
    
    # Description
    if item.get('short_description'):
        lines.append(item['short_description'])
        lines.append('')
    
    # Capabilities
    capabilities = item.get('capabilities', {})
    if capabilities:
        typical_workflows = capabilities.pop('typical_workflows', None)
        compute_software = capabilities.pop('compute_software_deps', None)
        
        if capabilities:
            lines.extend(['Capabilities', '------------', ''])
            for key, value in capabilities.items():
                label = key.replace('_', ' ').title()
                if isinstance(value, list) and len(value) > 1:
                    lines.append(f"**{label}:**")
                    lines.append('')
                    for v in value:
                        lines.append(f"- {v}")
                    lines.append('')
                else:
                    formatted = format_value(value)
                    lines.append(f"- **{label}:** {formatted}")
            lines.append('')
        
        # Typical workflows
        if typical_workflows:
            lines.extend(['Typical Workflow', '----------------', ''])
            for i, step in enumerate(typical_workflows, 1):
                lines.append(f"{i}. {step}")
            lines.append('')
        
        # Software requirements
        if compute_software:
            lines.extend(['Software Requirements', '---------------------', ''])
            for software in compute_software:
                lines.append(f"- {software}")
            lines.append('')
    
    # Availability notes
    if item.get('availability_notes'):
        lines.extend(['Availability Notes', '------------------', ''])
        lines.append(item['availability_notes'])
        lines.append('')
    
    # Training
    if item.get('training_required'):
        lines.extend(['Training Required', '-----------------', ''])
        lines.append('Yes - hands-on training is required before operating this equipment.')
        lines.append('')
        if item.get('training_link'):
            lines.append(f"Training materials: `{item['training_link']} <{item['training_link']}>`_")
            lines.append('')
    
    # Risk assessment
    if item.get('risk_assessment_required'):
        lines.extend(['Risk Assessment', '---------------', ''])
        lines.append('A risk assessment is required before using this equipment.')
        lines.append('')
    
    # Safety and constraints
    constraints = item.get('constraints', {})
    if constraints and constraints.get('notes'):
        lines.extend(['Safety and Operational Notes', '-----------------------------', ''])
        lines.append('.. warning::')
        lines.append('')
        lines.append(f"   {constraints['notes']}")
        lines.append('')
        
        if constraints.get('environment'):
            lines.append('**Environmental Requirements:**')
            lines.append('')
            for env in constraints['environment']:
                lines.append(f"- {env.replace('_', ' ').title()}")
            lines.append('')
        
        if constraints.get('safety_flags'):
            lines.append('**Safety Requirements:**')
            lines.append('')
            for flag in constraints['safety_flags']:
                lines.append(f"- {flag.replace('_', ' ').title()}")
            lines.append('')
    
    # Tags
    if item.get('tags'):
        lines.extend(['Tags', '----', ''])
        for tag in item['tags']:
            lines.append(f"``{tag}``  ")
        lines.append('')
    
    # Note
    contact = item.get('primary_contact', 'lab personnel')
    lines.append('.. note::')
    lines.append('')
    lines.append(f"   For more detailed information, contact {contact}.")
    lines.append('')
    
    return '\n'.join(lines)

def main():
    # Read equipment data
    json_path = 'docs/source/_static/data/equipment.json'
    with open(json_path) as f:
        data = json.load(f)
    
    equipment = data['equipment']
    created = []
    skipped = []
    
    for item in equipment:
        name = item['name']
        category = item.get('category', 'misc')
        
        # Determine directory
        dir_name = CATEGORY_TO_DIR.get(category, 'sensors')
        dir_path = f"docs/source/2-equipment/{dir_name}"
        
        # Create filename
        filename = clean_filename(name) + '.rst'
        filepath = os.path.join(dir_path, filename)
        
        # Skip if exists
        if os.path.exists(filepath):
            skipped.append((name, filepath))
            continue
        
        # Generate content
        content = generate_rst_content(item)
        
        # Write file
        os.makedirs(dir_path, exist_ok=True)
        with open(filepath, 'w') as f:
            f.write(content)
        
        created.append((name, filepath, dir_name))
    
    # Print summary
    print(f"Created {len(created)} equipment pages")
    print(f"Skipped {len(skipped)} existing pages")
    print()
    
    if created:
        print("Created pages:")
        for name, path, dir_name in created:
            print(f"  [{dir_name}] {name}")
    
    return created, skipped

if __name__ == '__main__':
    created, skipped = main()
